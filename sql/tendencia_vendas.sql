WITH vendas_mensais AS (
    SELECT 
        TO_CHAR(data_pedido, 'YYYY-MM') AS mes_ano,
        SUM(valor_total) AS total_vendas
    FROM pedidos
    GROUP BY mes_ano
)

SELECT 
    mes_ano,
    total_vendas,

    LAG(total_vendas) OVER (ORDER BY mes_ano) AS vendas_mes_anterior,

    ROUND(
    ((total_vendas - LAG(total_vendas) OVER (ORDER BY mes_ano)) 
    / LAG(total_vendas) OVER (ORDER BY mes_ano)) * 100, 2) AS crescimento_percentual

	

FROM vendas_mensais
ORDER BY mes_ano;