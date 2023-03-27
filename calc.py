# Definir função para adição
def add(num1, num2):
    return num1 + num2

# Definir função para subtração
def subtract(num1, num2):
    return num1 - num2

# Definir função para multiplicação
def multiply(num1, num2):
    return num1 * num2

# Definir função para divisão
def divide(num1, num2):
    if num2 == 0:
        return "Não é possível dividir por zero"
    else:
        return num1 / num2

# Pedir ao usuário o tipo de operação e os números para calcular
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Chamar a função correspondente à operação escolhida pelo usuário
if operacao == "+":
    print(num1, "+", num2, "=", add(num1, num2))
elif operacao == "-":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operacao == "*":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operacao == "/":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Operação inválida. Por favor, tente novamente.")
