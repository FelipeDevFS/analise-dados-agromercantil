CREATE INDEX idx_itens_pedido_id_pedido 
ON itens_pedido(id_pedido);

CREATE INDEX idx_pedidos_id_cliente 
ON pedidos(id_cliente);

CREATE INDEX idx_pedidos_data_pedido 
ON pedidos(data_pedido);