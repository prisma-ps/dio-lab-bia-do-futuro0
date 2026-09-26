# 🚀 Desenvolvimento do Mentor de Carteira com o Google Antigravity

Este documento descreve como o **Google Antigravity** foi utilizado como plataforma de desenvolvimento orientada a agentes (*AI-first pair programming*) para conceber, arquitetar, implementar, testar e estruturar o projeto **Mentor de Carteira** no desafio da [DIO](https://dio.me).

---

## 🎯 O Papel do Antigravity no Projeto

O **Google Antigravity** não atuou como um simples gerador de código, mas como um **parceiro de engenharia e mentoria técnica**. O processo seguiu o princípio da **autonomia do desenvolvedor**: discutir a estratégia de produto, validar premissas de negócio, refinar regras de segurança e construir uma solução pronta para o mercado financeiro.

```
       [Desenvolvedor] ──(Diretrizes de Negócio e Risco)──┐
                                                           ▼
                                               [Google Antigravity]
                                                ├── Análise de Contexto (DIO)
                                                ├── Engenharia de Prompts
                                                ├── Refinamento & Debugging
                                                └── Scaffolding Automatizado
                                                           │
                                                           ▼
                                            [Projeto "Mentor de Carteira"]
```

---

## 🛠️ Como o Antigravity Foi Utilizado nas 6 Etapas

### 1. Concepção e Regras de Negócio (Alinhamento Estratégico)
- **Desafio:** Definir o escopo para evitar um agente genérico ou perigoso que faz recomendações financeiras irregulares.
- **Atuação com Antigravity:** Através de um diálogo socrático, o desenvolvedor estabeleceu as regras de ouro:
  - Foco exclusivo em iniciantes e reserva de emergência.
  - Proibição absoluta de citar códigos/tickers pontuais (prevenção contra violação de suitability).
  - Tratamento consultivo e acolhedor para insistência em Renda Variável (a "Regra dos 15%").

### 2. Leitura e Integração da Base de Conhecimento
- **Desafio:** Entender o padrão do repositório de referência da DIO (`dio-lab-bia-do-futuro`) sem atrito.
- **Atuação com Antigravity:** O Antigravity inspecionou diretamente os dados e os templates do repositório da DIO via ferramentas nativas de leitura, garantindo que os esquemas de dados de `perfil_investidor.json` e `produtos_financeiros.json` fossem reaproveitados de forma compatível.

### 3. Engenharia de Prompts e Ajuste Fino (*Prompt Tuning*)
- **Desafio:** Garantir consistência nas respostas e evitar alucinações de identidade.
- **Atuação com Antigravity:**
  - Construção do **System Prompt** com seções de contexto, regras inegociáveis e exemplos *few-shot*.
  - **Detecção e Correção de Bug em Tempo Real:** Durante os testes práticos, foi identificada uma troca pontual de nome do cliente. O Antigravity auxiliou na análise da causa raiz (prioridade do input do chat vs. contexto do cadastro) e desenhou a **Regra de Identificação Mandatória**, blindando o agente.

### 4. Arquitetura da Aplicação Funcional (Python + Streamlit + Gemini)
- **Desafio:** Criar uma interface navegável, leve e funcional sem complexidade de infraestrutura.
- **Atuação com Antigravity:**
  - Apresentação do esqueleto conceitual explicando a separação de responsabilidades e o papel do `st.session_state` para memória do chat.
  - Integração com a SDK oficial do Google Gemini (`google-genai`), com configuração de temperatura baixa (`0.2`) para respostas determinísticas e seguras.
  - Inclusão de recursos amigáveis na interface, como inserção de API Key na barra lateral e exibição do perfil do cliente ativo.

### 5. Bateria de Testes Estruturados e Métricas de Qualidade
- **Desafio:** Provar empiricamente que o agente respeita as diretrizes de segurança.
- **Atuação com Antigravity:**
  - Desenho de cenários de teste desafiadores (tentativa de obter "dica quente", alocação inicial de R$ 500 e insistência em Renda Variável).
  - Execução dos testes e validação da capacidade matemática do modelo (cálculo correto da proporção de R$ 425 na segurança e R$ 75 em renda variável).
  - Estruturação do relatório formal de avaliação com 100% de taxa de conformidade.

### 6. Scaffolding e Organização do Repositório no Padrão DIO
- **Desafio:** Estruturar toda a documentação Markdown e o código conforme os templates da DIO.
- **Atuação com Antigravity:** Geração automatizada e precisa de todos os arquivos do projeto (`README.md`, `requirements.txt`, pastas `data/`, `docs/` e `src/app.py`), garantindo que nenhum item obrigatório do desafio ficasse de fora.

---

## 💡 Recursos do Antigravity que Fizeram a Diferença

| Recurso do Antigravity | Como foi aplicado no projeto |
|---|---|
| **Pair Programming Dialógico** | Condução orientada ao aprendizado: o agente propôs abordagens conceituais sem impor códigos fechados. |
| **Leitura Dinâmica de Contexto** | Consulta em tempo real aos repositórios e especificações do desafio da DIO. |
| **Scaffolding Multi-arquivo** | Criação atômica e consistente de toda a árvore de arquivos e diretórios do projeto. |
| **Auditoria e Ajuste Fino** | Diagnóstico rápido de desvios no comportamento da LLM e implementação de salvaguardas (*guardrails*). |

---

## 📈 Conclusão

O uso do **Google Antigravity** permitiu transformar uma ideia de negócio em uma aplicação funcional completa, testada e documentada em poucas iterações. Mais do que velocidade, o ambiente proporcionou **rigor técnico, clareza arquitetural e conformidade com as melhores práticas de IA do mercado**.
