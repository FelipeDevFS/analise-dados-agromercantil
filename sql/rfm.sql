WITH pedidos_cliente AS (
    SELECT 
        id_cliente,
        data_pedido,
        valor_total,

        COUNT(*) OVER (PARTITION BY id_cliente) AS total_pedidos,
        
        AVG(valor_total) OVER (PARTITION BY id_cliente) AS ticket_medio,

        LAG(data_pedido) OVER (PARTITION BY id_cliente ORDER BY data_pedido) AS pedido_anterior,

        MAX(data_pedido) OVER (PARTITION BY id_cliente) AS ultimo_pedido

    FROM pedidos
),
/* RECÊNCIA, FREQUÊNCIA E MONETÁRIO */
RFM_BASE AS (
	SELECT DISTINCT 
		id_cliente,
		total_pedidos,
		ticket_medio,
		ultimo_pedido,

		CURRENT_DATE - ultimo_pedido AS dias_desde_ultimo_pedido

		FROM pedidos_cliente
)
SELECT * FROM RFM_BASE;