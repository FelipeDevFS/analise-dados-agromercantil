import streamlit as st
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

from database import (
    get_top_produtos,
    get_kpis,
    get_tendencia_vendas,
    get_clientes_inativos,
    get_anomalias,
    get_rfm
)

# ================= CONFIG =================
st.set_page_config(
    page_title="Dashboard Agromercantil",
    layout="wide",
    initial_sidebar_state="expanded"
)




# ================= CSS SIMPLES =================
st.markdown("""
<style>
header {
    background-color: #000000 !important;
}
    .stAppDeployButton {display:none;}            
    .stApp {
        background-color: #030200;
    }

    section[data-testid="stSidebar"] {
        background-color: #4E7C28 !important;
    }

    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    h1 {
        color: #A8D053 !important;
        font-weight: 700;
    }

    h2, h3 {
        color: #FFFFFF !important;
    }

    [data-testid="stMetric"] {
        background-color: #132A13;
        border: 1px solid #4E7C28;
        padding: 15px;
        border-radius: 10px;
    }

    [data-testid="stMetricValue"] {
        color: #A8D053 !important;
        font-size: 24px !important;
    }
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.header("Filtros")

data_inicio = st.sidebar.date_input(
    "Data Inicial",
    value=date(2024, 1, 1)
)

data_fim = st.sidebar.date_input(
    "Data Final",
    value=date(2025, 12, 31)
)
# ================= CARREGAMENTO =================
with st.spinner("Carregando dados..."):
    kpis = get_kpis(data_inicio, data_fim)

    receita_total = kpis["receita_total"][0] or 0
    total_pedidos = kpis["total_pedidos"][0] or 0
    ticket_medio = kpis["ticket_medio"][0] or 0

    df_anomalias = get_anomalias(data_inicio, data_fim)
    total_anomalias = len(df_anomalias)

    df_produtos = get_top_produtos(data_inicio, data_fim)
    df_tendencia = get_tendencia_vendas(data_inicio, data_fim)
    df_inativos = get_clientes_inativos(data_fim)

    df_rfm = get_rfm()

# ================= HEADER =================
st.title("Dashboard Agromercantil")
st.caption("Análise de vendas, comportamento de clientes e detecção de inconsistências")

# ================= KPIs =================
col1, col2, col3, col4 = st.columns(4)

col1.metric("Receita Total", f"R$ {receita_total:,.2f}")
col2.metric("Pedidos", total_pedidos)
col3.metric("Ticket Médio", f"R$ {ticket_medio:,.2f}")
col4.metric("Anomalias", total_anomalias)

st.divider()

# ================= RFM =================
st.subheader("Análise RFM de Clientes")

if df_rfm.empty:
    st.info("Sem dados de clientes")
else:
    col1, col2 = st.columns(2)

    with col1:
        st.bar_chart(
            df_rfm.set_index("id_cliente")["total_pedidos"],
            color="#A8D053"
        )

    with col2:
        st.bar_chart(
            df_rfm.set_index("id_cliente",)["dias_desde_ultimo_pedido"],
            color="#F89923"
        )

    df_rfm = df_rfm.rename(columns={
        "id_cliente": "Cliente",
        "total_pedidos": "Pedidos",
        "ticket_medio": "Ticket Médio",
        "ultimo_pedido": "Último Pedido",
        "dias_desde_ultimo_pedido": "Dias sem comprar"
    })

    st.dataframe(df_rfm, use_container_width=True)

st.divider()

# ================= GRÁFICOS =================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Tendência de Vendas")

    if df_tendencia.empty:
        st.info("Sem dados para o período selecionado")
    else:
        st.line_chart(df_tendencia.set_index("mes_ano")["total_vendas"],  color="#A8D053")

with col2:
    st.subheader("Top 5 Produtos")

    if df_produtos.empty:
        st.info("Sem dados para o período selecionado")
    else:
        st.bar_chart(df_produtos.set_index("nome")["total_vendas"],  color="#A8D053")

st.divider()

# ================= TABELA PRODUTOS =================
st.subheader("Detalhamento dos Produtos")

if df_produtos.empty:
    st.info("Nenhum produto encontrado para o período selecionado")
else:
    df_produtos = df_produtos.rename(columns={
        "id_produto": "ID Produto",
        "nome": "Produto",
        "total_vendas": "Receita (R$)"
    })

    st.dataframe(df_produtos, use_container_width=True)

st.divider()

# ================= INATIVOS E ANOMALIAS =================
col1, col2 = st.columns(2)

with col1:
    st.subheader("Clientes Inativos")

    if df_inativos.empty:
        st.success("Nenhum cliente inativo")
    else:
        df_inativos = df_inativos.rename(columns={
            "id_cliente": "ID Cliente",
            "nome": "Nome",
            "ultimo_pedido": "Último Pedido"
        })

        st.dataframe(
            df_inativos.sort_values(by="Último Pedido"),
            use_container_width=True
        )

with col2:
    st.subheader("Anomalias")

    if df_anomalias.empty:
        st.success("Nenhuma inconsistência encontrada")
    else:
        df_anomalias = df_anomalias.rename(columns={
            "id_pedido": "ID Pedido",
            "valor_total_registrado": "Valor Registrado",
            "valor_calculado": "Valor Calculado"
        })

        st.warning(f"{len(df_anomalias)} inconsistências encontradas")
        st.dataframe(df_anomalias, use_container_width=True)




st.divider()
st.subheader("Análise Exploratória dos Dados")

if not df_tendencia.empty:

    # ================= HISTOGRAMA =================
    fig, ax = plt.subplots(figsize=(6,3))
    fig.patch.set_facecolor("#030200")
    ax.set_facecolor("#132A13")

    ax.hist(df_tendencia["total_vendas"])
    ax.set_title("Distribuição de Vendas", color="white")
    ax.set_xlabel("Valor", color="white")
    ax.set_ylabel("Frequência", color="white")
    ax.tick_params(colors="white")

    st.pyplot(fig, use_container_width=True)


    # ================= BOXPLOT =================
    fig, ax = plt.subplots(figsize=(6,3))
    fig.patch.set_facecolor("#030200")
    ax.set_facecolor("#132A13")

    ax.boxplot(df_tendencia["total_vendas"])
    ax.set_title("Boxplot de Vendas", color="white")
    ax.tick_params(colors="white")

    st.pyplot(fig, use_container_width=True)


    # ================= SCATTER =================
    fig, ax = plt.subplots(figsize=(6,3))
    fig.patch.set_facecolor("#030200")
    ax.set_facecolor("#132A13")

    ax.scatter(range(len(df_tendencia)), df_tendencia["total_vendas"])
    ax.set_title("Distribuição Temporal", color="white")
    ax.set_xlabel("Período", color="white")
    ax.set_ylabel("Vendas", color="white")
    ax.tick_params(colors="white")

    st.pyplot(fig, use_container_width=True)