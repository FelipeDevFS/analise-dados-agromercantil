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