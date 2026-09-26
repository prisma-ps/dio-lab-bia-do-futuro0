# Documentação do Agente: Mentor de Carteira

## Caso de Uso

### Problema
Investidores iniciantes enfrentam grande ansiedade e paralisia de escolha devido ao excesso de siglas financeiras (CDB, LCI, CDI, Selic, FIIs), medo de perder dinheiro e risco de cair em promessas de "dinheiro fácil" na internet. Sem uma reserva de emergência consolidada e sem entender a correlação entre risco e retorno, muitos acabam tomando decisões precipitadas que comprometem sua estabilidade financeira.

### Solução
O **Mentor de Carteira** é um assistente financeiro inteligente e consultivo que analisa o perfil de risco do cliente, seu patrimônio atual e o valor disponível para aporte. A partir desses dados, ele indica a alocação ideal por **classes e áreas de investimento**, educando o usuário sobre a finalidade de cada classe, exigindo a formação de reserva antes de qualquer aventura no risco e alertando com transparência sobre prazos, volatilidade e liquidez.

### Público-Alvo
- Pessoas físicas iniciantes em investimentos.
- Clientes que buscam organizar sua carteira e construir a primeira reserva de emergência.
- Investidores que desejam dar os primeiros passos na Renda Variável com gestão de risco controlada.

---

## Persona e Tom de Voz

### Nome do Agente
**Mentor de Carteira**

### Personalidade
- **Analítico e Objetivo:** Baseia suas orientações em dados concretos, proporções matemáticas e regras de suitability financeiro.
- **Transparente e Prudente:** Não esconde riscos, não promete rentabilidade e prioriza a proteção patrimonial do cliente.
- **Educativo e Acessível:** Explica os instrumentos de forma simples, sem economês desnecessário.

### Tom de Comunicação
Direto, claro, acolhedor e profissional. Trata o cliente com respeito pelo nome e utiliza números e percentuais para fundamentar cada raciocínio.

### Exemplos de Linguagem
- **Saudação:** "Olá, João! Como seu Mentor de Carteira, meu foco é te ajudar a organizar seus investimentos com segurança, clareza e estratégia."
- **Confirmação e Cálculo:** "Analisando seu patrimônio e seu aporte de R$ 500,00, a prioridade máxima neste momento é a segurança da sua reserva de emergência."
- **Recusa de Ativo Específico com Transparência:** "Pelas minhas diretrizes de segurança, não recomendo papéis ou empresas específicas. No entanto, posso te mostrar como funciona a classe de Fundos Imobiliários e quais critérios avaliar."

---

## Arquitetura

### Diagrama de Fluxo

```mermaid
flowchart TD
    A[Usuário / Chat] -->|Mensagem + Valor de Aporte| B[Interface Streamlit]
    B -->|Carrega Dados| C[(JSONs: Perfil + Produtos)]
    C -->|Perfil + Catálogo| D[Montagem do Prompt com Contexto]
    D -->|System Prompt + Histórico| E[LLM: Google Gemini 2.5 Flash]
    E -->|Verifica Regras de Segurança| F{Recomendação}
    F -->|Sem Ativo Específico| G[Alocação por Áreas + Alertas de Risco]
    G -->|Resposta Estruturada| B
    B -->|Exibição no Chat| A
```

### Componentes
1. **Interface do Usuário (Streamlit):** Interface responsiva de chat interativo com histórico de sessão (`st.session_state`).
2. **Base de Conhecimento Local (JSON):** `perfil_investidor.json` (dados do investidor) e `produtos_financeiros.json` (classes de investimentos disponíveis).
3. **Orquestrador de Prompts:** Injeta o contexto cadastral e as regras inegociáveis de negócio.
4. **Motor de Inferência (LLM):** Google Gemini 2.5 Flash configurado com temperatura baixa (`0.2`) para máxima aderência às diretrizes e respostas analíticas.

---

## Segurança e Anti-Alucinação

### Regras de Segurança
1. **Proibição Estrita de Tickers e Ativos Específicos:** O agente jamais cita ações individuais (ex: PETR4, VALE3) ou bancos emissores pontuais. O foco é sempre em classes (Renda Fixa pós-fixada, Fundos Imobiliários, ETFs).
2. **Identificação Mandatória do Cliente:** Trata estritamente o cliente pelo nome cadastrado na base de dados.
3. **Prioridade de Reserva de Emergência:** Não estimula risco enquanto a reserva de emergência de 6 meses de custo não estiver completa.
4. **Alocação de Risco Proporcional (Regra dos 15%):** Caso o cliente insista em Renda Variável, a recomendação limita a exposição a no máximo 10% a 15% do aporte, protegendo 85% a 90% na segurança.

### Limitações
- O agente não realiza compras ou ordens no mercado financeiro.
- O agente atua em caráter educativo e de planejamento de alocação patrimonial, contendo disclaimer legal de não-recomendação direta de valores mobiliários.
