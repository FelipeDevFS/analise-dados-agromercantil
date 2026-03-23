import pandas as pd
from sqlalchemy import create_engine

def get_connection():
    engine = create_engine("postgresql://postgres:root@localhost:5432/analise_agro")
    return engine

def get_top_produtos(data_inicio, data_fim):
    query = f"""
    WITH receita_produtos AS (
        SELECT
            ip.id_produto,
            p.nome,
            SUM(ip.quantidade * ip.preco_unitario) AS total_vendas
        FROM itens_pedido ip
        JOIN pedidos pe ON pe.id_pedido = ip.id_pedido
        JOIN produtos p ON p.id_produto = ip.id_produto
        WHERE pe.data_pedido BETWEEN '{data_inicio}' AND '{data_fim}'
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


def get_kpis(data_inicio, data_fim):
    query = f"""
    SELECT 
        SUM(valor_total) AS receita_total,
        COUNT(*) AS total_pedidos,
        AVG(valor_total) AS ticket_medio
    FROM pedidos
    WHERE data_pedido BETWEEN '{data_inicio}' AND '{data_fim}';
    """
    
    engine = get_connection()
    return pd.read_sql(query, engine)


def get_tendencia_vendas(data_inicio, data_fim):
    query = f"""
    WITH vendas_mensais AS (
        SELECT 
            TO_CHAR(data_pedido, 'YYYY-MM') AS mes_ano,
            SUM(valor_total) AS total_vendas
        FROM pedidos
        WHERE data_pedido BETWEEN '{data_inicio}' AND '{data_fim}'
        GROUP BY mes_ano
    )

    SELECT 
        mes_ano,
        total_vendas
    FROM vendas_mensais
    ORDER BY mes_ano;
    """
    
    engine = get_connection()
    return pd.read_sql(query, engine)

def get_clientes_inativos(data_limite):
    query = f"""
    SELECT 
        pe.id_cliente,
	    cli.nome,
        MAX(pe.data_pedido) AS ultimo_pedido
    FROM pedidos pe
    JOIN clientes cli
    ON cli.id_cliente = pe.id_cliente
    GROUP BY pe.id_cliente, cli.nome
    HAVING MAX(data_pedido) < '{data_limite}'::date - INTERVAL '6 months';
    """
    
    engine = get_connection()
    return pd.read_sql(query, engine)



def get_anomalias(data_inicio, data_fim):
    query = f"""
    WITH valores_calculados AS (
        SELECT 
            id_pedido,
            SUM(quantidade * preco_unitario) AS valor_calculado
        FROM itens_pedido
        GROUP BY id_pedido
    )

    SELECT 
        p.id_pedido,
        p.valor_total AS valor_total_registrado,
        vc.valor_calculado
    FROM pedidos p
    JOIN valores_calculados vc
        ON p.id_pedido = vc.id_pedido
    WHERE p.valor_total <> vc.valor_calculado
    AND p.data_pedido BETWEEN '{data_inicio}' AND '{data_fim}';
    """
    
    engine = get_connection()
    return pd.read_sql(query, engine)

def get_rfm():
    query = """
    WITH pedidos_cliente AS (
    SELECT 
        pe.id_cliente, 
        pe.data_pedido, 
        pe.valor_total, 
        cli.nome, 
        COUNT(*) OVER (PARTITION BY pe.id_cliente) AS total_pedidos, 
        ROUND(AVG(valor_total) OVER (PARTITION BY pe.id_cliente), 2) AS ticket_medio, 
        MAX(data_pedido) OVER (PARTITION BY pe.id_cliente) AS ultimo_pedido 
    FROM pedidos pe 
    JOIN clientes cli ON pe.id_cliente = cli.id_cliente 
), 
RFM_BASE AS (
    SELECT DISTINCT 
        id_cliente, 
        nome, 
        total_pedidos, 
        ticket_medio, 
        ultimo_pedido, 
        (CURRENT_DATE - ultimo_pedido) AS dias_desde_ultimo_pedido 
    FROM pedidos_cliente
) 
SELECT * FROM RFM_BASE ORDER BY ticket_medio ASC;
    """
    engine = get_connection()
    return pd.read_sql(query, engine)