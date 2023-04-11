
import json

produtos = []

def cadastrar_produto():
    print("\n# Cadastro de Produto\n")
    
    nome = input("Digite o nome do produto: ")
    valor_compra = float(input("Digite o valor de compra do produto: "))
    quantidade_estoque = int(input("Digite a quantidade em estoque do produto: "))
    
    codigo = len(produtos) + 1
    valor_venda = valor_compra * 1.25
    
    produto = {
        "codigo": codigo,
        "nome": nome,
        "valor_compra": valor_compra,
        "valor_venda": valor_venda,
        "quantidade_estoque": quantidade_estoque
    }
    
    produtos.append(produto)
    
    print("\nProduto cadastrado com sucesso!\n")
    
    return produtos


def relatorio_produtos():
    print("\n# Relatório de Produtos (ordenado por nome)\n")

    if not produtos:
        print("Não há produtos cadastrados.")
        return

    produtos_ordenados = sorted(produtos, key=lambda produto: produto["nome"])

    for produto in produtos_ordenados:
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Valor de compra: R${produto['valor_compra']:.2f}")
        print(f"Valor de venda: R${produto['valor_venda']:.2f}")
        print(f"Quantidade em estoque: {produto['quantidade_estoque']}\n")


def relatorio_estoque_baixo():
    print("\n# Relatório de Estoque Baixo\n")

    if not produtos:
        print("Não há produtos cadastrados.")
        return

    produtos_estoque_baixo = []

    for produto in produtos:
        if produto['quantidade_estoque'] <= 5:
            produtos_estoque_baixo.append(produto)

    if not produtos_estoque_baixo:
        print("Não há produtos com estoque baixo.")
        return

    for produto in produtos_estoque_baixo:
        print(f"Código: {produto['codigo']}")
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade em estoque: {produto['quantidade_estoque']}\n")


def exportar_json():
    with open('dados.json', 'w') as arquivo:
        json.dump(produtos, arquivo, indent=4)


opc = -1
while opc != 0:
    print("Varejão Trident")
    print("[1] Cadastrar produto")
    print("[2] Relatório de produtos")
    print("[3] Relatório de Estoque Baixo")
    print("[4] Exportar dados")
    print("[0] Sair")

    opc = int(input("Digite uma opção: "))

    if opc == 1:
        cadastrar_produto()

    elif opc == 2:
        relatorio_produtos()

    elif opc == 3:
        relatorio_estoque_baixo()

    elif opc == 4:
        exportar_json()

print("Programa encerrado.")


# import datetime
# import locale

# locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# data_atual = datetime.datetime.now()

# print("Data atual:", data_atual)

# ano_atual = data_atual.year

# print("Ano atual:", ano_atual)

# mes_atual = data_atual.month

# print("Mês atual:", mes_atual)

# dia_atual = data_atual.day

# print("Dia atual:", dia_atual)

# data_formatada_brasil = data_atual.strftime('%d/%m/%Y')

# print("Data atual formatada (Brasil):", data_formatada_brasil)

# data_formatada_extenso = data_atual.strftime('%d de %B de %Y')

# print("Data atual formatada (extenso):", data_formatada_extenso)
