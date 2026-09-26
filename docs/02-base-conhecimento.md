# Base de Conhecimento

## Dados Utilizados

O agente utiliza arquivos estruturados em formato JSON localizados na pasta `data/` para fundamentar suas análises sem depender de alucinações da LLM:

| Arquivo | Formato | Papel no Agente |
|---------|---------|-----------------|
| `perfil_investidor.json` | JSON | Fornece a identidade do cliente (João Silva), sua renda mensal, patrimônio acumulado, saldo da reserva de emergência e tolerância ao risco. |
| `produtos_financeiros.json` | JSON | Catálogo de classes e modalidades de investimento, com métricas de rentabilidade estimada, liquidez de resgate, valor de aporte mínimo e público indicado. |

---

## Estrutura dos Arquivos

### 1. `perfil_investidor.json`
Contém os parâmetros de suitability do cliente atendido:
```json
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false
}
```

### 2. `produtos_financeiros.json`
Categoriza as opções por áreas de investimentos e parâmetros de risco:
```json
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "liquidez": "D+1",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "liquidez": "D+0",
    "aporte_minimo": 100.00,
    "indicado_para": "Reserva de emergência e liquidez diária"
  },
  {
    "nome": "Fundos Imobiliários (FIIs - Base)",
    "categoria": "renda_variavel",
    "risco": "medio",
    "rentabilidade": "Rendimento mensal de aluguéis / cota oscilante",
    "liquidez": "D+2 (mercado secundário)",
    "aporte_minimo": 10.00,
    "indicado_para": "Diversificação e renda passiva de longo prazo"
  },
  {
    "nome": "ETFs de Índice de Ações",
    "categoria": "renda_variavel",
    "risco": "alto",
    "rentabilidade": "Variação do índice de mercado de ações",
    "liquidez": "D+2 (mercado secundário)",
    "aporte_minimo": 50.00,
    "indicado_para": "Crescimento patrimonial de longo prazo (3 a 5 anos+)"
  }
]
```

---

## Estratégia de Injeção de Contexto

Para garantir que o agente não invente informações cadastrais ou produtos inexistentes:
1. **Carregamento Determinístico:** Os arquivos JSON são lidos diretamente no início da execução da aplicação Python.
2. **Context Window Injection:** O conteúdo dos JSONs é convertido em string formatada e injetado diretamente nas `system_instruction` da chamada ao Google Gemini.
3. **Cruzamento Lógico:** O prompt obriga o modelo a comparar a `reserva_emergencia_atual` com a meta (6x `renda_mensal`) antes de liberar sugestões de outras classes de maior volatilidade.
