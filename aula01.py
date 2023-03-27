#
s = "aeiou"

#print(s[0])
#print(s[-2])
#print(s[0]*20)
#print('a' in s)
#print('x' not in s)
#print(s[0:2])
#print(s[2:])
#print(s[:2])
#print(s[:])

#func auxiliar

s1='Abcdefg   '

#print(chr(65))
#print(ord(s1[0]))
#print(repr(s1))
#print(len(s1))
#print(len(s1.strip()))
#print(s1.upper())
#print(s1.lower())
#print(s1.capitalize())

a=1
b=2

#print(a+b)

#print(a-b)

#print(a*b)

#print(a/b)

#print(a//b)

#print(a%b)

#print(a**b)



a=10
b=20

#print(a==b)
#print(a!=b)
#print(a>b)
#print(a>=b)
#print(a<b)
#print(a<=b)

import os 
os.system('cls')

#nome = input("Qual seu nome ?")
#print("Olá," ,nome, " seja bem vindo!")

#msg = "Olá, {} seja bem vindo!".format(nome)
#print(msg)

#n1= int(input("entre com o primeiro valor:  ")) 
#n2= int(input("entre com o primeiro valor:  "))
#soma=n1+n2
#print(f"soma: {round(soma,1)}")

##str1= "Joao da Silva"
##for c in str1:
##    print(c ,end='')

# EX1
#altura = float(input("informe a altura do seu triangulo:  "))
#base = float(input("informe a base do seu triangulo:  "))
#Area = (base*altura)/2
#print(f" A area do seu tringulo é de: {Area}")

#EX2

#peso = float(input("informe seu peso:  "))
#altura = float(input("informe sua altura(ex 1.52):  "))
#imc=round((peso/(altura*altura)),2)

#if imc >25 and imc <= 29.9:
 #    print(f"Seu IMC é : {imc} e voce esta com sobrepeso")

#elif imc >30 and imc <= 34.9:
 #    print(f"Seu IMC é :{imc} e voce esta com Obesidade grau 1")

#elif imc >35 and imc <= 39.9:
 #    print(f"Seu IMC é :{imc} e voce esta com Obesidade grau 2")

#elif imc > 40:
#     print(f"Seu IMC é :{imc} e voce esta com Obesidade grau 3")     


#EX3

nome_prod = input("informe o nome do produto:  ")
valor_prod = float(input("informe o valor do produto:  "))
novo_valor = (valor_prod + (valor_prod * 0.12))

print(f" O(a) {nome_prod} possuia o valor {valor_prod} e com o acrecimo de 12% foi para :  {novo_valor}")