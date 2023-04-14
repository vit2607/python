# Victor Augusto Wittner
# RM: 98667

print("Seja Bem-Vindo a Vinheira Agnello")

Nome = input("Digite seu nome:")
Idade = int(input("Digite sua idade:"))
if Idade < 18:
    print("Desculpe, não podemos prosseguir com a sua compra, é necessario ser maior de idade para realiar compras")
    exit()
Endereço_do_Cliente = input("Digite o seu endereço:")
Endereço_de_Entrega = input("Digite seu endereço de entrega:")

print("Nosso catalogo de vinhos a seguir:")
carrinho = {}
catalogo_vinhos = {
    "Vinho 1 "'R$': 50.00,
    "Vinho 2 "'R$': 100.00,
    "Vinho 3 "'R$': 150.00,
    "Vinho 4 "'R$': 75.00,
    "Vinho 5 "'R$': 125.00,
}
opcao = 1
while opcao <= len(catalogo_vinhos):
    vinho = f"Vinho {opcao} R$"
    preco = catalogo_vinhos[vinho]
    print(f"{vinho} - R$ {preco:.2f}")
    opcao += 1

print("Por favor, informe a quantidade de vinhos que deseja comprar de cada opção:")
opcao = 1
total_pedido = 0
while opcao <= len(catalogo_vinhos):
    vinho = f"Vinho {opcao} R$"
    preco = catalogo_vinhos[vinho]
    quantidade = int(input(f"{vinho} - R$ {preco:.2f}: "))
    total_item = preco * quantidade
    total_pedido += total_item
    carrinho[vinho] = quantidade
    opcao += 1

print(f"Total do pedido: R$ {total_pedido:.2f}")
    
if total_pedido < 100:
    print("O valor mínimo de compra é de R$ 100,00. Por favor, adicione mais produtos ao seu pedido.")
else:
    frete = 20.00
    if total_pedido > 200:
        print("Parabéns, você ganhou frete grátis!")
    else:
        print(f"O valor do frete é de R$ {frete:.2f}")
        total_pedido += frete


print(f"Total do pedido: R$ {total_pedido:.2f}")

print("Seu carrinho:")

for vinho, quantidade in carrinho.items():
    print(f"{vinho}: {quantidade}")
    
print(f"Total do pedido: R$ {total_pedido:.2f}")
print(f"Endereço de entrega: {Endereço_de_Entrega}")
print("Obrigado pela sua compra, volte sempre!")
    
    













