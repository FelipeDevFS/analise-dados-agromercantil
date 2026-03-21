WITH ultimo_pedido_cliente AS (
SELECT 
    id_cliente,
    MAX(data_pedido) AS ultimo_pedido
FROM pedidos
GROUP BY id_cliente
)

SELECT id_cliente, 
	   ultimo_pedido
FROM ultimo_pedido_cliente
WHERE ultimo_pedido < DATE '2025-03-01' - INTERVAL '6 months';