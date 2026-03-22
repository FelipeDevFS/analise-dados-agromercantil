# 📊 Estratégia de Mock de Dados

Os dados foram estruturados para simular diferentes perfis de clientes:

- Cliente recorrente com alto volume de compras
- Cliente ocasional com compras moderadas
- Cliente inativo sem compras recentes
- Cliente novo com poucas compras

Além disso:

- Foram criadas variações de produtos por categoria e faixa de preço
- Os pedidos foram distribuídos ao longo de diferentes meses para
  permitir análise temporal
- Foi incluída uma inconsistência proposital entre o valor total do
  pedido e a soma dos itens, com o objetivo de possibilitar a detecção
  de anomalias

---

# 🧠 Alteração do Modelo de Dados

Atualmente, o modelo de dados permite que cada pedido esteja associado a
apenas um cliente, por meio da chave estrangeira `id_cliente` na tabela
`pedidos`.

Para permitir que um pedido tenha múltiplos clientes (como em cenários
de compras compartilhadas), é necessário transformar esse relacionamento
em N:N (muitos para muitos).

Para isso, propõe-se a criação de uma tabela intermediária chamada
`clientes_pedidos`, responsável por associar clientes e pedidos.

Além disso, a coluna `id_cliente` seria removida da tabela `pedidos`,
eliminando a dependência direta entre as entidades e garantindo maior
flexibilidade no modelo.

Essa abordagem evita redundância e garante que o relacionamento entre
clientes e pedidos seja controlado de forma adequada pela tabela
intermediária.
