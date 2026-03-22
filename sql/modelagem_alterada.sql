-- Remover relacionamento direto (conceitualmente)
-- ALTER TABLE pedidos DROP COLUMN id_cliente;

-- Nova tabela de relacionamento N:N
CREATE TABLE clientes_pedidos (
    id_cliente INT,
    id_pedido INT,
    PRIMARY KEY (id_cliente, id_pedido),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
);