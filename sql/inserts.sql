-- CLIENTES
INSERT INTO clientes (nome, data_cadastro) VALUES
('João Silva', '2023-01-10'),   -- cliente antigo e ativo
('Maria Souza', '2023-03-15'),  -- cliente médio
('Carlos Pereira', '2022-11-20'), -- cliente antigo (vai virar inativo)
('Ana Costa', '2024-01-05');    -- cliente novo

-- PRODUTOS
INSERT INTO produtos (nome, categoria, preco) VALUES
('Fertilizante Premium', 'Fertilizantes', 200),
('Fertilizante Básico', 'Fertilizantes', 100),
('Semente Milho', 'Sementes', 50),
('Semente Soja', 'Sementes', 70),
('Defensivo Agrícola', 'Defensivos', 300);

-- PEDIDOS
INSERT INTO pedidos (data_pedido, valor_total, id_cliente) VALUES
('2024-08-10', 400, 1),
('2024-09-15', 200, 2),
('2024-10-01', 600, 1),
('2024-11-20', 150, 2),
('2024-12-05', 800, 1),
('2025-01-10', 100, 4),
('2025-02-12', 500, 1),
('2025-03-01', 300, 2),
('2024-06-10', 250, 3); -- cliente inativo

-- ITENS DOS PEDIDOS
INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario) VALUES
(1, 1, 2, 200),
(2, 3, 4, 50),
(3, 5, 2, 300),
(4, 2, 1, 100),
(5, 1, 4, 200),
(6, 3, 2, 50),
(7, 5, 1, 300),
(8, 4, 3, 70),
(9, 2, 2, 100),

-- ANOMALIA (valor errado de propósito)
(8, 1, 1, 200); 