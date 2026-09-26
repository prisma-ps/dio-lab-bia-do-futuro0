# 🤖 Mentor de Carteira - Agente Financeiro Inteligente

Projeto desenvolvido para o Lab **"Construa Seu Assistente Virtual Com Inteligência Artificial"** da [DIO](https://dio.me).

O **Mentor de Carteira** é um assistente financeiro consultivo, analítico e transparente, projetado para orientar investidores iniciantes na alocação de seu patrimônio, com foco em priorização de reserva de emergência, educação por classes de ativos e gestão proporcional de risco.

---

## 📌 Estrutura do Projeto

O repositório segue estritamente o padrão solicitado pela DIO:

```text
lab-agente-financeiro/
│
├── README.md                          # Visão geral do projeto
├── requirements.txt                   # Dependências Python
│
├── data/                              # Base de conhecimento local
│   ├── perfil_investidor.json         # Perfil e situação financeira do cliente
│   └── produtos_financeiros.json      # Catálogo de classes e produtos financeiros
│
├── docs/                              # Documentação completa dos 6 passos
│   ├── 01-documentacao-agente.md      # Caso de uso, persona e arquitetura
│   ├── 02-base-conhecimento.md        # Dados e estratégia de injeção de contexto
│   ├── 03-prompts.md                  # Engenharia de prompts e edge cases
│   ├── 04-metricas.md                 # Avaliação, testes estruturados e resultados
│   └── 05-pitch.md                    # Roteiro cronometrado do pitch de 3 minutos
│
└── src/                               # Aplicação funcional
    └── app.py                         # Chatbot interativo com Streamlit e Gemini
```

---

## 🛡️ Diferenciais e Regras de Segurança

- **Zero Recomendação Específica:** O agente nunca indica ações ou tickers pontuais (cumprindo requisitos éticos de suitability).
- **Educação por Classes:** Indica áreas de investimento (Renda Fixa pós-fixada, Fundos Imobiliários, ETFs) explicando seus instrumentos e riscos associados.
- **Prioridade de Reserva:** 100% dos aportes são direcionados à liquidez até a conclusão da meta da reserva de emergência.
- **Gestão Proporcional (Regra dos 15%):** Caso o cliente insista em Renda Variável, a exposição é limitada com segurança a no máximo 10%-15% do aporte.

---

## 🚀 Como Executar a Aplicação

### 1. Clonar ou Acessar a Pasta do Projeto
```bash
cd lab-agente-financeiro
```

### 2. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar a Chave de API
Você pode obter uma chave gratuita no [Google AI Studio](https://aistudio.google.com/). Configure-a no ambiente ou insira diretamente na barra lateral da aplicação:
```bash
export GEMINI_API_KEY="sua_chave_aqui"
```

### 4. Executar o Streamlit
```bash
streamlit run src/app.py
```

A interface abrirá automaticamente no seu navegador padrão (`http://localhost:8501`).
