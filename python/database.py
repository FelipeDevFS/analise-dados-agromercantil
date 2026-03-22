import pandas as pd
from sqlalchemy import create_engine

def get_connection():
    engine = create_engine("postgresql://postgres:root@localhost:5432/analise_agro")
    return engine

def get_top_produtos():
    query = """
    WITH receita_produtos AS (
        SELECT
            ip.id_produto,
            p.nome,
            SUM(ip.quantidade * ip.preco_unitario) AS total_vendas
        FROM itens_pedido ip
        JOIN pedidos pe ON pe.id_pedido = ip.id_pedido
        JOIN produtos p ON p.id_produto = ip.id_produto
        GROUP BY ip.id_produto, p.nome
    )
    SELECT 
        id_produto, 
        nome, 
        total_vendas
    FROM receita_produtos
    ORDER BY total_vendas DESC
    LIMIT 5;
    """
    
    engine = get_connection()
    return pd.read_sql(query, engine)


def get_kpis():
    query = """
    SELECT 
        SUM(valor_total) AS receita_total,
        COUNT(*) AS total_pedidos,
        AVG(valor_total) AS ticket_medio
    FROM pedidos;
    """
    
    engine = get_connection()
    return pd.read_sql(query, engine)

