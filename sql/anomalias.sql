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
WHERE p.valor_total <> vc.valor_calculado;