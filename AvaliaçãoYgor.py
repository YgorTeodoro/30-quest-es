
print('Questão 1')
# Soma de 2 números: : Peça ao usuário dois números e mostre a soma deles.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calculando a soma
soma = numero1 + numero2

# Mostrando o resultado
print("A soma de", numero1, "e", numero2, "é:", soma)

print('Questão 2')
# Subtração de dois números: Peça ao usuário dois números e mostre a subtração do primeiro pelo segundo.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calculando a subtração
subtracao = numero1 - numero2

# Mostrando o resultado
print("A subtração de", numero1, "pelo", numero2, "é:", subtracao)

print('Questão 3')
 # Multiplicação de dois números: Peça ao usuário dois números e mostre o resultado da multiplicação entre eles.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calculando a multiplicação
multiplicacao = numero1 * numero2

# Mostrando o resultado
print("A multiplicação de", numero1, "e", numero2, "é:", multiplicacao)

print('Questão 4')
#Divisão de dois números: Peça ao usuário dois números e mostre o resultado da divisão do primeiro pelo segundo. 
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calculando a divisão
divisao = numero1 / numero2
# Mostrando o resultado
print("A divisão de", numero1, "pelo", numero2, "é:", divisao)

print('Questão 5')
# Resto da divisão: Peça dois números inteiros e mostre o resto da divisão entre eles.
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Verificando se o segundo número é diferente de zero para evitar divisão por zero
if numero2 != 0:
    # Calculando o resto da divisão
    resto = numero1 % numero2
    # Mostrando o resultado
    print("O resto da divisão de", numero1, "por", numero2, "é:", resto)
else:
    print("Erro: Não é possível dividir por zero.")

print('Questão 6')
#  Potência de um número: Peça um número e um expoente, e mostre o resultado do número elevado a esse expoente.
numero = float(input("Digite um número: "))
expoente = int(input("Digite o expoente: "))

# Calculando a potência
resultado = numero ** expoente

# Mostrando o resultado
print(f"O resultado de {numero} elevado a {expoente} é: {resultado}")

print('Questão 7')
# Média de três: Peça três números e mostre a média deles.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

# Calculando a média
media = (numero1 + numero2 + numero3) / 3

# Mostrando o resultado
print(f"A média dos três números é: {media}")

print('Questão 8')
#  Conversão de temperatura: Converta uma temperatura em graus Celsius para Fahrenheit usando a fórmula:
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Convertendo para Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Mostrando o resultado
print(f"A temperatura em graus Fahrenheit é: {fahrenheit}")
print('Questão 09')
# Conversão de moeda: Peça um valor em reais e mostre o valor convertido em doláres.
# Taxa de conversão fixa
taxa_conversao = 5.00

# Pedindo ao usuário para inserir um valor em reais
reais = float(input("Digite o valor em reais: "))

# Convertendo para dólares
dolares = reais / taxa_conversao

# Mostrando o resultado
print(f"O valor em dólares é: {dolares:.2f}")

print('Questão 10')
# Área de um retângulo: Peça a largura e a altura de um retângulo e calcule a área.
largura = float(input("Digite a largura do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

# Calculando a área
area = largura * altura

# Mostrando o resultado
print(f"A área do retângulo é: {area}")

print('Questão 11')
# Perímetro de um quadrado: Peça o lado de quadrado e calcule o perímetro (Soma dos lados).
def calcular_perimetro(lado):
    return 4 * lado

# Solicitar o comprimento do lado do quadrado ao usuário
lado_quadrado = float(input("Digite o comprimento do lado do quadrado: "))

# Calcular o perímetro
perimetro = calcular_perimetro(lado_quadrado)

# Exibir o resultado
print(f"O perímetro do quadrado é: {perimetro:.2f}")


print('Questão 12')
# Área do triangulo: Peça a base e a altura de um triângulo e calcule a área usando a fórmula:

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

# Calculando a área
area = (base * altura) / 2

# Mostrando o resultado
print(f"A área do triângulo é: {area}")

print('Questão 13')
# Área de um círculo: Peça o raio de um círculo e calcule a área usando a fórmula:  Aˊrea=πr2\text{Área} = \pi r^2Aˊrea=πr2 (Use o valor aproximado de π = 3.14159)
# Função para calcular a área de um círculo
def calcular_area_circulo(raio):
    pi = 3.14159
    return pi * (raio ** 2)

# Solicitar o raio do círculo ao usuário
raio_circulo = float(input("Digite o raio do círculo: "))

# Calcular a área
area = calcular_area_circulo(raio_circulo)

# Exibir o resultado
print(f"A área do círculo é: {area:.2f}")


print('Questão 14')
# Conversão de metros para centímetros: Peça um valor em metros e converta 
def metros_para_centimetros(metros):
    return metros * 100

# Solicitar um valor em metros ao usuário
valor_metros = float(input("Digite o valor em metros: "))

# Realizar a conversão
valor_centimetros = metros_para_centimetros(valor_metros)

# Exibir o resultado
print(f"{valor_metros} metros é igual a {valor_centimetros} centímetros.")

print('Questão 15')
# Cálculo de horas trabalhadas: Peça a quantidade de horas trabalhadas e o valor por hora, e calcule o salário total.

def calcular_salario(horas_trabalhadas, valor_por_hora):
    return horas_trabalhadas * valor_por_hora

# Solicitar a quantidade de horas trabalhadas e o valor por hora ao usuário
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: "))

# Realizar o cálculo do salário
salario_total = calcular_salario(horas_trabalhadas, valor_por_hora)

# Exibir o resultado
print(f"O salário total é: R$ {salario_total:.2f}")

print('Questão 16')
# Preço com desconto: Peça o preço de um produto e o percentual de desconto, e mostre o preço final com desconto aplicado.
def calcular_preco_com_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final

# Solicitar o preço do produto e o percentual de desconto ao usuário
preco = float(input("Digite o preço do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Calcular o preço final com desconto
preco_final = calcular_preco_com_desconto(preco, percentual_desconto)

# Exibir o resultado
print(f"O preço final com desconto é: R$ {preco_final:.2f}")

print('Questão 17')
# Calcular a velocidade média: Peça a distância percorrida e o tempo gasto, e calcule a velocidade média usando a fórmula: 
def calcular_velocidade_media(distancia, tempo):
    if tempo <= 0:
        return "O tempo deve ser maior que zero."
    return distancia / tempo

# Solicitar a distância percorrida e o tempo gasto ao usuário
distancia = float(input("Digite a distância percorrida (em km): "))
tempo = float(input("Digite o tempo gasto (em horas): "))

# Calcular a velocidade média
resultado = calcular_velocidade_media(distancia, tempo)

# Exibir o resultado
if isinstance(resultado, str):
    print(resultado)
else:
    print(f"A velocidade média é: {resultado:.2f} km/h")

print('Questão 18')
#  Converter idade em dias: Peça a idade de uma pessoa em anos e converta para dias. Desconsidere anos bissextos.
def idade_em_dias(idade_anos):
    return idade_anos * 365

# Solicitar a idade em anos ao usuário
idade_anos = int(input("Digite a sua idade em anos: "))

# Calcular a idade em dias
idade_dias = idade_em_dias(idade_anos)

# Exibir o resultado
print(f"Sua idade em dias é: {idade_dias} dias.")

print('Questão 19')
#  Quantidade de segundos em um dia: Calcule quantos segundos existem em um dia (24 horas).
def segundos_em_um_dia():
    horas_por_dia = 24
    minutos_por_hora = 60
    segundos_por_minuto = 60
    return horas_por_dia * minutos_por_hora * segundos_por_minuto

# Calcular a quantidade de segundos em um dia
total_segundos = segundos_em_um_dia()

# Exibir o resultado
print(f"A quantidade de segundos em um dia é: {total_segundos} segundos.")

print('Questão 20')
# Calcular o IMC (Índice de Massa Corporal): Peça o peso (em kg) e a altura (em metros), e calcule o IMC usando a fórmula: 
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Solicitar o peso e a altura ao usuário
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))

# Calcular o IMC
imc = calcular_imc(peso, altura)

# Exibir o resultado
print(f"O seu IMC é: {imc:.2f}")

print('Questão 21')
# Diferença entre dois números: Peça dois números e mostre a diferença absoluta entre eles (sem sinal negativo).
def diferença_absoluta(num1, num2):
    return abs(num1 - num2)

# Solicitar os dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calcular a diferença absoluta
resultado = diferença_absoluta(numero1, numero2)

# Exibir o resultado
print(f"A diferença absoluta entre os números é: {resultado}")

print('Questão 22')
# Divisão inteira de dois números: Peça dois números inteiros e mostre o resultado da divisão inteira (sem considerar o resto).
def divisao_inteira(num1, num2):
    return num1 // num2

# Solicitar os dois números inteiros ao usuário
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Verificar se o segundo número é zero para evitar divisão por zero
if numero2 == 0:
    print("Erro: Não é possível dividir por zero.")
else:
    # Calcular a divisão inteira
    resultado = divisao_inteira(numero1, numero2)
    
    # Exibir o resultado
    print(f"O resultado da divisão inteira é: {resultado}")

print('Questão 23')
# Valor absoluto de um número: Peça um número e mostre seu valor absoluto.
def valor_absoluto(num):
    return abs(num)

# Solicitar um número ao usuário
numero = float(input("Digite um número: "))

# Calcular o valor absoluto
resultado = valor_absoluto(numero)

# Exibir o resultado
print(f"O valor absoluto de {numero} é: {resultado}")

print('Questão 24')
# . Converter km/h para m/s: Peça uma velocidade em km/h e converta para m/s. Use a fórmula:

def converter_kmh_para_mps(velocidade_kmh):
    return velocidade_kmh / 3.6

# Solicitar a velocidade em km/h ao usuário
velocidade_kmh = float(input("Digite a velocidade em km/h: "))

# Calcular a velocidade em m/s
velocidade_mps = converter_kmh_para_mps(velocidade_kmh)

# Exibir o resultado
print(f"A velocidade em m/s é: {velocidade_mps:.2f} m/s")

print('Questão 25')
# Fórmula de Bhaskara: Peça os coeficientes aaa, bbb e ccc de uma equação do segundo grau e calcule as raízes usando a fórmula de Bhaskara.

import math
# Função para calcular as raízes usando a fórmula de Bhaskara
def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return None  # Raízes complexas
    elif delta == 0:
        raiz = -b / (2 * a)
        return (raiz,)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return (raiz1, raiz2)

# Solicitar os coeficientes a, b e c ao usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calcular as raízes
raizes = calcular_raizes(a, b, c)

# Exibir o resultado
if raizes is None:
    print("As raízes são complexas.")
elif len(raizes) == 1:
    print(f"A raiz dupla é: {raizes[0]:.2f}")
else:
    print(f"As raízes são: {raizes[0]:.2f} e {raizes[1]:.2f}")

print('Questão 26')
#Valor total de uma compra: Peça o preço de três produtos e calcule o valor total da compra. 
def calcular_total(preco1, preco2, preco3):
    return preco1 + preco2 + preco3

# Solicitar os preços dos produtos ao usuário
preco_produto1 = float(input("Digite o preço do primeiro produto: R$ "))
preco_produto2 = float(input("Digite o preço do segundo produto: R$ "))
preco_produto3 = float(input("Digite o preço do terceiro produto: R$ "))

# Calcular o valor total da compra
valor_total = calcular_total(preco_produto1, preco_produto2, preco_produto3)

# Exibir o resultado
print(f"O valor total da compra é: R$ {valor_total:.2f}")

print('Questão 27')
# Converter dias para semanas e dias: Peça um valor em dias e converta para semanas e dias (por exemplo, 10 dias = 1 semana e 3 dias).
def converter_dias(dias):
    semanas = dias // 7
    dias_restantes = dias % 7
    return semanas, dias_restantes

# Solicitar o valor em dias ao usuário
dias = int(input("Digite o número de dias: "))

# Calcular semanas e dias
semanas, dias_restantes = converter_dias(dias)

# Exibir o resultado
print(f"{dias} dias é igual a {semanas} semanas e {dias_restantes} dias.")

print('Questão 28')
#  Desconto progressivo: Peça o valor de uma compra e aplique um desconto de 5% se o valor for maior que R$100, e de 10% se for maior que R$500.
def calcular_desconto(valor):
    if valor > 500:
        desconto = valor * 0.10  # 10% de desconto
    elif valor > 100:
        desconto = valor * 0.05  # 5% de desconto
    else:
        desconto = 0  # Sem desconto
    
    return valor - desconto

# Solicitar o valor da compra ao usuário
valor_compra = float(input("Digite o valor da compra: R$ "))

# Calcular o valor final com desconto
valor_final = calcular_desconto(valor_compra)

# Exibir o resultado
print(f"O valor final da compra é: R$ {valor_final:.2f}")

print('Questão 29')
#  Divisão com casas decimais limitadas: Peça dois números e mostre o resultado da divisão com apenas duas casas decimais
def divisao_com_duas_casas_decimais(num1, num2):
    return num1 / num2

# Solicitar os dois números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verificar se o segundo número é zero para evitar divisão por zero
if numero2 == 0:
    print("Erro: Não é possível dividir por zero.")
else:
    # Calcular o resultado da divisão
    resultado = divisao_com_duas_casas_decimais(numero1, numero2)
    
    # Exibir o resultado com duas casas decimais
    print(f"O resultado da divisão é: {resultado:.2f}")



































