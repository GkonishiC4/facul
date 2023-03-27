# x1= float(input("informe o Valor 1: "))
# x2= float(input("informe o Valor 2: "))
# op = input("opercao{+,-,*,/}: ")


# if op =='+':
#     res = x1+x2

# elif op =='-':
#     res = x1-x2

# elif op =='*':
#     res = x1*x2

# elif op =='/':
#     if x1>0:
#         res = x1/x2
#     else: print("impossivel dividir por 0")

# print(res)



# import os
# os.system('cls')
# nome = "Joao da Silva"

# for letra in nome:
#     print(letra)

# import os
# os.system('cls')

# for i in range(5):
#     print(i)

# for i in range(1,10,2):
#     print(i)

# for i in range(1,10,-1):
#     print(i)

# soma = 0
# for i in range(5):
#      soma=+i
# else:print("soma = %d" %soma)

# dados = "abcdefg"
# for pos , valor in enumerate(dados):
#     print("Posicao: {0}, valor: {1}".format(pos,valor))

# for i in range(10):
#     if i >= 5 and i <=8:
#         continue
#     print(i)

#exercicio 1
# try:
#     prd = input("Informe o produto: ")
#     valor_prod = float(input("Informe o valor do produto: "))
# except ValueError:
#     print("Valor informado não é um número válido.")
# else:
#     if valor_prod >= 50 and valor_prod < 200:
#         desconto = valor_prod - (valor_prod * 0.05)
#         print("Valor do produto com desconto:", desconto)
#     elif valor_prod >= 200 and valor_prod < 500:
#         desconto = valor_prod - (valor_prod * 0.05)
#         print("Valor do produto com desconto:", desconto)
#     elif valor_prod >= 500 and valor_prod < 1000:
#         desconto = valor_prod - (valor_prod * 0.07)
#         print("Valor do produto com desconto:", desconto)
#     elif valor_prod >= 1000:
#         desconto = valor_prod - (valor_prod * 0.08)
#         print("Valor do produto com desconto:", desconto)
#     else:
#         print(f"O produto não teve desconto: {valor_prod}")

#exercicio 2
# list =[]
# for i in range(4):
#     valor = int(input("Digite o valor de uma resistencia: "))
#     list.append(valor)
# maior = max(list)
# menor = min(list)
# soma = sum(list)
# print(f"A resistencia com menor valor é :{menor}")
# print(f"A resistencia com maior valor é :{maior}")
# print(f"A soma da maior e da menor resistencia é :{soma}")

#exercicio 3

# numero = int(input("Digite o número desejado: "))
# for i in range(1, 11):
#     resultado = numero * i
#     print(numero, "x", i, "=", resultado)

#exercicio 4
# def century(year):
#     if year % 100 == 0:
#         century = year // 100
#     else:
#         century = year // 100 + 1
#     return century
# print(century(11))


# import os 
# def limpa_tela():
#     os.system('cls')

# # def ler_num():
# #     return int(input("Informa um valor: "))

# # def plus(n1,n2):
# #     return n1+n2

# # def main():
# #     limpa_tela()
# #     n1=ler_num()
# #     n2=ler_num()
# #     print(plus(n1,n2))
# # main()

# # def exibir_intervalo(ini = 0, fim =10, step =1):
# #     for i in range(ini,fim,step):
# #         print(i)

# # exibir_intervalo(1,10,2)
# # exibir_intervalo(0,200,10)


# # def exib_val(*val):
# #     for i in val:
# #         print(i)

# # exib_val(10,20,30,0,0,0,0,0,0,0,0,0,0,0,0)


# # Exercício 1
# # – Elabore uma aplicação receba um número 
# # indeterminado de valores informados pelo 
# # usuário.
# # – Crie funções para determinar:
# # • Quantidade de números pares
# # • Quais são os números ímpares
# # • O maior número
# # • O menor número
# # • A média dos números
# # – Apresente os resultados na tela.


# # def quantidade_pares(numeros):
# #     pares = [n for n in numeros if n % 2 == 0]
# #     return len(pares)

# # def numeros_impares(numeros):
# #     impares = [n for n in numeros if n % 2 != 0]
# #     return impares

# # def maior_numero(numeros):
# #     return max(numeros)

# # def menor_numero(numeros):
# #     return min(numeros)

# # def media(numeros):
# #     return sum(numeros)/len(numeros)

# # numeros = []
# # while True:
# #     num = input("Digite um número ou pressione ENTER para finalizar: ")
# #     if num == "":
# #         break
# #     numeros.append(int(num))

# # qtd_pares = quantidade_pares(numeros)
# # impares = numeros_impares(numeros)
# # maior = maior_numero(numeros)
# # menor = menor_numero(numeros)
# # media_num = media(numeros)

# # print(f"Quantidade de números pares: {qtd_pares}")
# # print(f"Números ímpares: {impares}")
# # print(f"Maior número: {maior}")
# # print(f"Menor número: {menor}")
# # print(f"Média dos números: {media_num}")


# # Exercício 2
# # – Elabore uma aplicação capaz de gerar o currículo 
# # de uma pessoa em HTML.
# # – Os parâmetros para o currículo são: nome, 
# # endereço, telefone, e-mail, escolaridade e 
# # experiência profissional.
# # – Você pode utilizar as tags HTML da sua 
# # preferência.
# # – Utilize funções para organizar o código fonte da 
# # aplicação.

# # # to open/create a new html file in the write mode
# # f = open('curriculo.html', 'w')

# # # the html code which will go in the file GFG.html
# # html_template = """<html>
# # <head>
# # <title>curriculo</title>
# # </head>
# # <body>
# # <h1>Nome</h1>
# # <p>NA</p>
# # <h2>endereço</h2>
# # <p>NA</p>
# # <h2>telefone</h2>
# # <p>NA</p>
# # <h2>e-mail</h2>
# # <p>NA</p>
# # <h2>escolaridade</h2>
# # <p>NA</p>
# # <h2>experiência profissional</h2>
# # <p>NA</p>
# # </body>
# # </html>
# # """

# # # writing the code into the file
# # f.write(html_template)

# # # close the file
# # f.close()

# import os 
# os.system('cls')

# html=f"""
# <h1><b>Nome:</b>{input("Entre com o nome: ")}<h1>
# <h2><b>endereço:</b>{input("Entre com o endereço: ")}<h2>
# <h2><b>telefone:</b>{input("Entre com o telefone: ")}<h2>
# <h2><b>e-mail:</b>{input("Entre com o e-mail: ")}<h2>
# <h2><b>escolaridade:</b>{input("Entre com a escolaridade: ")}<h2>
# <h2><b>experiência profissional:</b>{input("Entre com a experiência profissional: ")}<h2>
# """
# arquivo = open("teste.html",'w')
# arquivo.write(html)
# arquivo.close()
