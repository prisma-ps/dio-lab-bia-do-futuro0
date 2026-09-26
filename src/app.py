import os
import json
import streamlit as st
from google import genai

# ==============================================================================
# CONFIGURAÇÃO DA PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="Mentor de Carteira - Assistente Financeiro",
    page_icon="📈",
    layout="centered"
)

# ==============================================================================
# CARREGAMENTO DA BASE DE CONHECIMENTO
# ==============================================================================
@st.cache_data
def carregar_dados():
    """Lê os arquivos JSON da base de conhecimento com caminhos relativos robustos."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    caminho_perfil = os.path.join(base_dir, "data", "perfil_investidor.json")
    caminho_produtos = os.path.join(base_dir, "data", "produtos_financeiros.json")

    with open(caminho_perfil, "r", encoding="utf-8") as f:
        perfil = json.load(f)

    with open(caminho_produtos, "r", encoding="utf-8") as f:
        produtos = json.load(f)

    return perfil, produtos

# ==============================================================================
# CONSTRUÇÃO DO SYSTEM PROMPT COM AS REGRAS INEGOCIÁVEIS
# ==============================================================================
def construir_system_prompt(perfil, produtos):
    """Monta as instruções do agente com dados do cliente e regras de segurança."""
    return f"""Você é o Mentor de Carteira, um assistente financeiro analítico, objetivo e 100% transparente, focado em educar e orientar investidores iniciantes.

---
### 📌 BASE DE CONHECIMENTO DISPONÍVEL

1. DADOS DO CLIENTE CADASTRADO:
- Nome: {perfil['nome']}
- Perfil declarado: {perfil['perfil_investidor']}
- Renda mensal: R$ {perfil['renda_mensal']}
- Patrimônio total: R$ {perfil['patrimonio_total']}
- Reserva de emergência atual: R$ {perfil['reserva_emergencia_atual']}
- Aceita risco: {perfil['aceita_risco']}

2. CLASSES E PRODUTOS NA PRATELEIRA:
{json.dumps(produtos, ensure_ascii=False, indent=2)}

---
### 🛡️ SUAS REGRAS INEGOCIÁVEIS (DIRETRIZES DE SEGURANÇA)

1. REGRA DE IDENTIFICAÇÃO DO CLIENTE:
   - Trate sempre o cliente estritamente pelo nome registrado nos dados do cadastro ({perfil['nome']}).
   - Nunca invente, presuma ou alterne para outros nomes, a menos que o usuário solicite explicitamente no chat ("me chame de X").

2. PROIBIÇÃO DE RECOMENDAÇÃO ESPECÍFICA:
   - É expressamente proibido citar nomes de empresas, bancos emissores específicos ou códigos de negociação/tickers (ex: NÃO diga "compre PETR4", "compre o CDB do Banco X").
   - Fale sempre em termos de classes/áreas de investimento (ex: Renda Fixa pós-fixada com liquidez diária, Fundos Imobiliários, ETFs de índice).

3. EXPLICAÇÃO E ALERTA DE RISCO OBRIGATÓRIOS:
   - Para toda área ou classe citada, explique brevemente os tipos de ativos que existem nela e aponte os riscos reais (liquidez, oscilação diária ou impacto da inflação).

4. TRATAMENTO EM CASO DE INSISTÊNCIA EM RENDA VARIÁVEL:
   - Se o cliente insistir em Renda Variável mesmo após os alertas, acolha o interesse educadamente.
   - Explique o conceito de Renda Variável (oscilação diária, sem rentabilidade garantida, horizonte de longo prazo).
   - Sugira uma gestão de risco proporcional (manter 85% a 90% na segurança e alocar apenas 10% a 15% do valor informado para aprender).
   - Indique as categorias conceituais (como ETFs amplos ou FIIs), mantendo a regra de jamais citar ativos específicos.

5. OBJETIVIDADE E TRANSPARÊNCIA:
   - Apresente cálculos claros, divisões percentuais e linguagem direta para iniciantes, sem jargões desnecessários.
"""

# ==============================================================================
# INTERFACE PRINCIPAL
# ==============================================================================
def main():
    st.title("📈 Mentor de Carteira")
    st.caption("Assistente consultivo de alocação e educação financeira para iniciantes")

    # Configuração da Chave de API na barra lateral
    api_key_env = os.environ.get("GEMINI_API_KEY", "")
    with st.sidebar:
        st.header("⚙️ Configurações")
        api_key_input = st.text_input(
            "Google Gemini API Key:",
            value=api_key_env,
            type="password",
            help="Obtenha sua chave gratuita em https://aistudio.google.com/"
        )
        st.divider()
        st.markdown("**Cliente Ativo:**")
        perfil, produtos = carregar_dados()
        st.write(f"👤 **Nome:** {perfil['nome']}")
        st.write(f"🎯 **Perfil:** {perfil['perfil_investidor'].capitalize()}")
        st.write(f"💰 **Patrimônio:** R$ {perfil['patrimonio_total']:,.2f}")
        st.write(f"🛡️ **Reserva Atual:** R$ {perfil['reserva_emergencia_atual']:,.2f}")

    chave_final = api_key_input or api_key_env
    if not chave_final:
        st.warning("⚠️ Insira sua Gemini API Key na barra lateral para iniciar a conversa.")
        return

    # Inicialização do Cliente Gemini
    client = genai.Client(api_key=chave_final)
    system_prompt = construir_system_prompt(perfil, produtos)

    # Histórico de Sessão
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = [
            {
                "role": "assistant",
                "content": f"Olá, {perfil['nome']}! Sou o seu **Mentor de Carteira**. Como posso te ajudar a planejar ou investir seu dinheiro hoje?"
            }
        ]

    # Exibição do histórico de mensagens
    for msg in st.session_state.mensagens:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Entrada do Usuário
    if prompt_usuario := st.chat_input("Digite sua dúvida sobre investimentos ou valor de aporte..."):
        # Registra e exibe a mensagem do usuário
        st.session_state.mensagens.append({"role": "user", "content": prompt_usuario})
        with st.chat_message("user"):
            st.markdown(prompt_usuario)

        # Monta o histórico recente para a LLM
        conversa_formatada = ""
        for m in st.session_state.mensagens:
            conversa_formatada += f"{m['role'].upper()}: {m['content']}\n"

        # Chamada ao modelo Gemini
        with st.chat_message("assistant"):
            with st.spinner("Analisando perfil e classes de ativos..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=conversa_formatada,
                        config={
                            "system_instruction": system_prompt,
                            "temperature": 0.2
                        }
                    )
                    texto_resposta = response.text
                except Exception as e:
                    texto_resposta = f"❌ Ocorreu um erro ao consultar o assistente: {str(e)}"

                st.markdown(texto_resposta)
                st.session_state.mensagens.append({"role": "assistant", "content": texto_resposta})

if __name__ == "__main__":
    main()
