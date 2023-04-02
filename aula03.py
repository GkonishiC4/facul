# tam = 6
# vetor=[0] * tam

# for i in range(tam):
#     vetor[i] = int(input(f"informe o {i+1} numero : "))

# num_par = 0
# num_impar = []
# soma=0
# maior = vetor[0]
# menor=[0]
# num_positivo=0

# for valor in vetor:
#     if valor % 2==0:
#         num_par += 1
#     else:
#         num_impar.append(valor)
#     soma += valor
#     if valor > maior:
#         maior = valor
#     if valor < menor:
#         menor = valor
#     if valor >0:
#         num_positivo += 1

# print(f"Qnt de num pares: {num_par}")
# print(f"Qnt de num impar: {num_impar}")
# print(f"Soma dos num: {soma}")
# print(f"O maior valor : {maior}")
# print(f"O menor valor : {menor}")
# print(f"Qnt de num positivos: {num_positivo}")


# #exec 2
# import random

# dimensao = 10

# imagem = [[0] * dimensao for _ in range(dimensao)]

# for i in range(dimensao):
#     for j in range(dimensao):
#         imagem[i][j] = random.randint(0, 255)

# for i in range(dimensao):
#     for j in range(dimensao):
#         print(f"{imagem[i][j]:3}", end=" ")
#     print()


# #exec 3
# aprovados=0
# exames=0
# reprovados=0
# soma_notas=0

# quantidade=int(input("Digite a quantidade de alunos: "))

# print(f"{'Nome':<10} {'N1':<5} {'N2':<5} {'Média':<7} {'Situação':<10}")


# for i in range(quantidade):

#     nome = input(f"Digite o nome do aluno {i+1}: ")
#     n1 = float(input(f"Digite a nota 1 do aluno {nome}: "))
#     n2 = float(input(f"Digite a nota 2 do aluno {nome}: "))
#     media = (n1+n2)/2
#     situacao = ""

#     if media >= 7:
#         situacao = "Aprovado"
#         aprovados += 1
#     elif media >= 4:
#         situacao = "Exame"
#         exames += 1
#     else:
#         situacao = "Reprovado"
#         reprovados += 1

#     print(f"{nome:<10} {n1:<5.1f} {n2:<5.1f} {media:<7.1f} {situacao:<10}")

#     soma_notas += media

# media_classe = soma_notas/quantidade
# print(f"Média da classe: {media_classe:.1f}")

# print(f"Quantidade de alunos aprovados: {(aprovados/quantidade)*100} %")
# print(f"Quantidade de alunos em exame: {(exames/quantidade)*100} %")
# print(f"Quantidade de alunos reprovados: {(reprovados/quantidade)*100} %")


# exec 4
# prd=[]

# for i in range(5):
#     nome = input(f"Digite o nome do produto {i+1}: ")
#     preco = float(input(f"Digite o preço do produto {nome}: "))
#     prd.append((nome,preco))

# abaixo_50 = 0
# entre_50_100 = 0
# acima_100 = 0

# for produto in prd:
#     if produto[1] < 50:
#         abaixo_50 += 1
#     elif produto[1] >= 50 and produto[1] <= 100:
#         entre_50_100 += 1
#     else:
#         acima_100 += 1

# print(f"Produtos abaixo de R$50: {abaixo_50}")
# print(f"Produtos entre R$50 e R$100: {entre_50_100}")
# print(f"Produtos acima de R$100: {acima_100}")


# lista

# exe 1

# def is_palindrome(palavra):
#      palavra = palavra.lower()
#      palavra = palavra.replace(" ","")
#      palavra = palavra.replace(",","")
#      palavra = palavra.replace(".","")
#      palavra = palavra.replace("?","")
#      palavra = palavra.replace("!","")
#      palavra = palavra.replace("@","")
#      palavra = palavra.replace("","")
#      palavra = palavra.replace("$","")
#      palavra = palavra.replace("%","")
#      palavra = palavra.replace("^","")
#      palavra = palavra.replace("&","")
#      palavra = palavra.replace("*","")
#      palavra = palavra.replace("-","")
#      palavra = palavra.replace("_","")
#      palavra = palavra.replace("+","")
#      palavra = palavra.replace("=","")
#      palavra = palavra.replace("/","")
#      palavra = palavra.replace("{","")
#      palavra = palavra.replace("}","")
#      palavra = palavra.replace("|","")
#      palavra = palavra.replace("~","")
#      palavra = palavra.replace("´","")
#      palavra = palavra.replace("`","")
#      palavra = palavra.replace("^","")
#      return palavra == palavra[::-1]


# print(is_palindrome("arara"))
# print(is_palindrome("A dama admirou o rim da amada"))


# exe 2
# vetor=[]

# for i in range(15):
#     valor = int(input(f"Digite o valor da posição {i}: "))
#     vetor.append(valor)

# maior_valor = max(vetor)

# for i in range(len(vetor)):
#     vetor[i] /= maior_valor

# print("Valores após os cálculos:")
# for valor in vetor:
#     print(valor)


# #exec 3
def adjacent_elements_product(input_array):
    return max(a * b for a, b in zip(input_array, input_array[1:]))

input_array = [3, 6, -2, -5, 7, 3]
largest_product = adjacent_elements_product(input_array)
print(largest_product)

# dicionario
# exec1
# import random
# import string

# alunos = ["Ana Maria", "João Silva", "Maria Santos", "Carlos Roberto"]

# usuarios = {}

# for aluno in alunos:
#     partes = aluno.split()
#     primeiro_nome = partes[0]
#     sobrenome = partes[-1]

# username = primeiro_nome[0].lower() + sobrenome.lower()
# if username in usuarios:
#      username += str(random.randint(1, 100))


# caracteres = string.ascii_letters + string.digits + string.punctuation
# senha = ''.join(random.choice(caracteres) for i in range(8))

    
# usuarios[username] = senha

# for username, senha in usuarios.items():
#      print("Username: " + username + " - Senha: " + senha)


# #exec1.1
# import random
# import string

# alunos = ["Ana Maria", "João Silva", "Maria Santos", "Carlos Roberto","Letícia Souza Pereira","Camila Cardoso Fernandes","Mariana Lima Almeida","Igor Melo Cardoso","Fabricio Gustavo Henrique"]
# usuarios = {}

# for aluno in alunos:
#      partes = aluno.split()
#      primeiro_nome = partes[0]
#      sobrenome = partes[-1]

#      username = primeiro_nome[0].upper() + sobrenome.lower()
#      if username in usuarios: 
#          username += str(random.randint(1, 100))

#      caracteres = string.ascii_letters + string.digits + string.punctuation
#      senha = ''.join(random.choice(caracteres) for i in range(32))

#      usuarios[aluno] = {'username': username, 'senha': senha}

# usuarios_ordenados = dict(sorted(usuarios.items()))

# for nome, dados in usuarios_ordenados.items():
#      print(f"Nome: {nome}\nUsername: {dados['username']}\nSenha: {dados['senha']}\n")


# import pandas as pd 

# usuarios_ordenados_csv = pd.DataFrame(usuarios_ordenados)
# print(usuarios_ordenados_csv)

# usuarios_ordenados_csv.to_csv("teste1.csv")

# import csv
# import random
# import string

# nomes = ['Maria', 'João', 'Ana', 'Pedro', 'Carlos', 'Mariana', 'Lucas', 'Luisa', 'Gustavo', 'Julia']
# sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Pereira', 'Ferreira', 'Gonçalves', 'Ribeiro', 'Almeida', 'Martins']

# alunos = []
# for i in range(100):
#     nome = random.choice(nomes)
#     sobrenome = random.choice(sobrenomes)
#     nome_completo = f"{nome} {sobrenome}"
#     alunos.append(nome_completo)

# usuarios = {} 
# usernames_gerados = set()

# for aluno in alunos:
#     partes = aluno.split()
#     primeiro_nome = partes[0]
#     sobrenome = partes[-1]

#     username = primeiro_nome[0].upper() + sobrenome.lower()
#     contador = 0
#     while username in usernames_gerados: 
#         contador += 1
#         username = primeiro_nome[0].upper() + sobrenome.lower() + str(contador)

#     usernames_gerados.add(username)  # adiciona o username gerado ao conjunto de usernames já gerados

#     caracteres = string.ascii_letters + string.digits + string.punctuation
#     senha = ''.join(random.choice(caracteres) for i in range(16))

#     usuarios[aluno] = {'username': username, 'senha': senha}

# usuarios_ordenados = dict(sorted(usuarios.items()))

# with open('usuarios131.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Nome', 'Username', 'Senha'])
#     for nome, dados in usuarios_ordenados.items():
#         writer.writerow([nome, dados['username'], dados['senha']])
