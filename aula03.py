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
# aprovados = 0
# exames = 0 
# reprovados = 0 
# soma_notas = 0 

# quantidade = int(input("Digite a quantidade de alunos: "))

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

# print(f"Quantidade de alunos aprovados: {aprovados}")
# print(f"Quantidade de alunos em exame: {exames}")
# print(f"Quantidade de alunos reprovados: {reprovados}")


#exec 4
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



## lista 

# exe 1 

def is_palindrome(palavra):
    palavra = palavra.lower()
    palavra = palavra.replace(" ","")
    palavra = palavra.replace(",","")
    palavra = palavra.replace(".","")
    palavra = palavra.replace("?","")
    palavra = palavra.replace("!","")
    palavra = palavra.replace("@","")
    palavra = palavra.replace("#","")
    palavra = palavra.replace("$","")
    palavra = palavra.replace("%","")
    palavra = palavra.replace("^","")
    palavra = palavra.replace("&","")
    palavra = palavra.replace("*","")
    palavra = palavra.replace("-","")
    palavra = palavra.replace("_","")
    palavra = palavra.replace("+","")
    palavra = palavra.replace("=","")
    palavra = palavra.replace("/","")
    palavra = palavra.replace("{","")
    palavra = palavra.replace("}","")
    palavra = palavra.replace("|","")
    palavra = palavra.replace("~","")
    palavra = palavra.replace("´","")
    palavra = palavra.replace("`","")
    palavra = palavra.replace("^","")
    return palavra == palavra[::-1]


print(is_palindrome("arara")) 
print(is_palindrome("A Rita, sobre vovo, verbos atira")) 



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

# #exe2
# vetor = []

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
# def adjacentElementsProduct(inputArray):
#     maior_produto = float('-inf') 

#     for i in range(len(inputArray)-1):
#         produto_atual = inputArray[i] * inputArray[i+1] 
#         if produto_atual > maior_produto: 
#             maior_produto = produto_atual

#     return maior_produto

# inputArray = [3, 6, -2, -5, 7, 3]
# largest_product = adjacentElementsProduct(inputArray)
# print(largest_product)

#dicionario
#exec1
# import random
# import string

# alunos = ["Ana Maria", "João Silva", "Maria Santos", "Carlos Roberto"]

# usuarios = {}

# for aluno in alunos:
#     partes = aluno.split()
#     primeiro_nome = partes[0]
#     sobrenome = partes[-1]

    
#     username = primeiro_nome[0].lower() + sobrenome.lower()
#     if username in usuarios:
#         username += str(random.randint(1, 100))

    
#     caracteres = string.ascii_letters + string.digits + string.punctuation
#     senha = ''.join(random.choice(caracteres) for i in range(8))

    
#     usuarios[username] = senha


# for username, senha in usuarios.items():
#     print("Username: " + username + " - Senha: " + senha)


#exec1.1
# import random
# import string

# alunos = ["Ana Maria", "João Silva", "Maria Santos", "Carlos Roberto"]

# usuarios = {}

# for aluno in alunos:
#     partes = aluno.split()
#     primeiro_nome = partes[0]
#     sobrenome = partes[-1]

#     username = primeiro_nome[0].lower() + sobrenome.lower()
#     if username in usuarios: 
#         username += str(random.randint(1, 100))

#     caracteres = string.ascii_letters + string.digits + string.punctuation
#     senha = ''.join(random.choice(caracteres) for i in range(8))

#     usuarios[aluno] = {'username': username, 'senha': senha}

# usuarios_ordenados = dict(sorted(usuarios.items()))

# for nome, dados in usuarios_ordenados.items():
#     print(f"Atividade Prática\nNome: {nome}\nUsername: {dados['username']}\nSenha: {dados['senha']}\n")
