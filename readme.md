# Dashboard de Análise de Dados - Agromercantil

## 📊 Objetivo

Este projeto tem como objetivo desenvolver uma solução completa de análise de dados utilizando PostgreSQL e Python (Streamlit), contemplando desde a modelagem e manipulação dos dados até a visualização interativa dos resultados.

A aplicação permite analisar o comportamento de clientes, desempenho de produtos e identificar inconsistências nos dados de vendas.

---

## 🧱 Estrutura do Projeto

- `sql/` → Scripts SQL com todas as consultas analíticas
- `python/` → Aplicação Streamlit
- `database.py` → Conexão com banco e queries
- `app.py` → Dashboard principal
- `docs/` → Prints da aplicação e consultas

---

## 🗄️ Banco de Dados

O banco foi estruturado com as seguintes tabelas:

- **clientes**
- **produtos**
- **pedidos**
- **itens_pedido**

O modelo segue um padrão relacional com chaves primárias e estrangeiras, permitindo análises consistentes e escaláveis.

---

## 🎯 Estratégia de Mock de Dados

Os dados foram inseridos manualmente com o objetivo de simular um cenário real de negócio, incluindo:

- Clientes recorrentes com alto volume de compras
- Clientes ocasionais
- Clientes inativos
- Clientes novos

Além disso:

- Foram criadas diferentes categorias de produtos
- Houve variação de preços e quantidades
- Os pedidos foram distribuídos ao longo de vários meses para permitir análise temporal
- Foi inserida uma inconsistência proposital entre o valor total do pedido e a soma dos itens, permitindo análise de anomalias

Os dados foram distribuídos entre os períodos de **2024 e 2025**, sendo este o intervalo considerado para análise no dashboard.

---

## 📈 Análises SQL

Foram desenvolvidas consultas utilizando:

- CTEs (Common Table Expressions)
- Funções de janela (COUNT, AVG, LAG)
- Agregações e filtros

### Principais análises:

- **RFM (Recência, Frequência e Monetário)**
- **Top 5 produtos mais rentáveis**
- **Tendência de vendas mensal**
- **Clientes inativos (mais de 6 meses)**
- **Detecção de anomalias em pedidos**

---

## 🔄 Alteração do Modelo de Dados

Para permitir que um pedido tenha múltiplos clientes (compras compartilhadas), foi proposta a transformação do relacionamento para N:N.

Alterações sugeridas:

- Remoção da coluna `id_cliente` da tabela `pedidos`
- Criação de uma tabela intermediária `clientes_pedidos`

```sql
CREATE TABLE clientes_pedidos (
    id_cliente INT,
    id_pedido INT,
    PRIMARY KEY (id_cliente, id_pedido),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
);
```

Essa abordagem elimina redundância e aumenta a flexibilidade do modelo.

---

## ⚡ Otimização e Indexação

Foram sugeridos índices para melhorar a performance das consultas:

```sql
CREATE INDEX idx_pedidos_cliente ON pedidos(id_cliente);
CREATE INDEX idx_pedidos_data ON pedidos(data_pedido);
CREATE INDEX idx_itens_pedido ON itens_pedido(id_pedido);
```

Esses índices melhoram:

- Performance de joins
- Filtros por data
- Execução de agregações

---

## 🖥️ Dashboard (Streamlit)

A aplicação foi desenvolvida utilizando Streamlit e apresenta:

- KPIs principais (Receita, Pedidos, Ticket Médio e Anomalias)
- Gráficos de tendência de vendas
- Ranking de produtos mais rentáveis
- Análise RFM de clientes
- Tabela detalhada de produtos
- Lista de clientes inativos
- Detecção de anomalias

Também foi implementado:

- Filtro por período (padronizado conforme os dados disponíveis entre 2024 e 2025)
- Layout tematizado com base na identidade visual da Agromercantil

---

## 📊 Análise Exploratória

Utilizando Pandas e Matplotlib:

- Histograma para distribuição de vendas
- Boxplot para identificação de outliers
- Scatter plot para análise temporal

Essas análises complementam os insights obtidos nas consultas SQL.

---

## ▶️ Como Executar

1. Instale as dependências:

```
pip install -r requirements.txt
```

2. Execute a aplicação:

```
streamlit run python/app.py
```

---

## 📸 Evidências

Os prints das consultas SQL e da aplicação estão disponíveis na pasta:

```
/docs
```

---

## ✅ Conclusão

O projeto demonstra a construção de um pipeline completo de análise de dados, desde a modelagem até a visualização, utilizando boas práticas de SQL, Python e visualização interativa.

Foram aplicados conceitos importantes como:

- Funções de janela
- Modelagem relacional
- Detecção de inconsistências
- Análise de comportamento de clientes

A solução entrega uma visão clara e prática para tomada de decisão baseada em dados.
