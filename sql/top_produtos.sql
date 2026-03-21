WITH receita_produtos AS (
    SELECT
        ip.id_produto,
        p.nome,
        ROUND(SUM(ip.quantidade * ip.preco_unitario), 2) AS total_vendas
    FROM itens_pedido ip
    JOIN pedidos pe ON pe.id_pedido = ip.id_pedido
    JOIN produtos p ON p.id_produto = ip.id_produto
    WHERE pe.data_pedido >= DATE '2025-03-01' - INTERVAL '1 year'
    GROUP BY ip.id_produto, p.nome
)

SELECT 
    id_produto, 
    nome, 
    total_vendas
FROM receita_produtos
ORDER BY total_vendas DESC
LIMIT 5;