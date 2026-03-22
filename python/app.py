import streamlit as st
from database import get_top_produtos, get_kpis

st.title("Dashboard Agromercantil")

# KPIs no topo
kpis = get_kpis()

receita_total = kpis["receita_total"][0]
total_pedidos = kpis["total_pedidos"][0]
ticket_medio = kpis["ticket_medio"][0]

col1, col2, col3 = st.columns(3)
col1.metric("Receita Total", f"R$ {receita_total:.2f}")
col2.metric("Total de Pedidos", total_pedidos)
col3.metric("Ticket Médio", f"R$ {ticket_medio:.2f}")

st.divider()

# Top produtos
st.subheader("Top 5 Produtos Mais Rentáveis")

df = get_top_produtos()

st.bar_chart(df.set_index("nome")["total_vendas"])

st.caption("Tabela detalhada dos produtos")
st.dataframe(df)
