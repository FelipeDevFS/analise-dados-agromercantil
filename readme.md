# 📊 Dashboard de Análise de Dados - Agromercantil

## 📊 Objetivo

Este projeto tem como objetivo desenvolver uma solução completa de
análise de dados utilizando **PostgreSQL** e **Python (Streamlit)**,
contemplando desde a modelagem e manipulação dos dados até a
visualização interativa dos resultados.

A aplicação permite analisar o comportamento de clientes, desempenho de
produtos e identificar inconsistências nos dados de vendas.

---

## 🧱 Estrutura do Projeto

    sql/        → Scripts SQL com todas as consultas analíticas
    python/     → Aplicação Streamlit
      ├── database.py → Conexão com banco e queries
      └── app.py      → Dashboard principal
    docs/       → Prints da aplicação e consultas

---

## 🗄️ Banco de Dados

- clientes
- produtos
- pedidos
- itens_pedido

---

## 🎯 Estratégia de Mock de Dados

- Clientes recorrentes com alto volume de compras\
- Clientes ocasionais\
- Clientes inativos\
- Clientes novos

📅 Dados entre **2024 e 2025**

---

## 📈 Análises SQL

- RFM\
- Top 5 produtos\
- Tendência mensal\
- Clientes inativos\
- Anomalias

---

## ▶️ Como Executar

    pip install -r requirements.txt
    streamlit run python/app.py

---

## ✅ Conclusão

Projeto completo de análise de dados com SQL + Python + Streamlit.
