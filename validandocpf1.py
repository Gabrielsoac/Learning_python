#validando CPF:

import re 
import sys

cpf_titular = input('Digite o seu CPF: ')
cpf_titular = re.sub(r'[^0-9]', '', cpf_titular) #expressão regular para tratar possíveis erros

nove_digitos_cpf = cpf_titular[:9] #início do cálculo do primeiro dígito
auxiliar = 10 #usa-se 10 digitos como auxiliar no primeiro dígito
aprovado = None

cpf_e_sequencial = cpf_titular == cpf_titular[0] * len(cpf_titular)

if cpf_e_sequencial:
    print('O CPF digitado é sequencial e inválido')
    sys.exit()

soma = 0
for digito in nove_digitos_cpf: #looping para realizar multiplicação e soma do resultado para lista
    soma += int(digito) * auxiliar
    auxiliar = auxiliar - 1

digito_1 = (soma * 10) % 11 #digito 1 receberá o restante da divisão por 11

digito_1 = digito_1 if digito_1 <= 9 else 0 #condicional

dez_digitos = cpf_titular[:10] #início do cálculo do segundo dígito adicionando o primeiro

auxiliar_2 = 11 #usa-se 11 dígitos como auxiliar no segundo dígito

soma2 = 0
for digito in dez_digitos: #looping para realizar multiplicação e soma do resultado para lista
    soma2 += int(digito) * auxiliar_2
    auxiliar_2 = auxiliar_2 - 1

digito_2 = (soma2 * 10) % 11

digito_2 = digito_2 if digito_2 <= 9 else 0

if cpf_titular[-1] == str(digito_2) and cpf_titular[-2] == str(digito_1):
    aprovado = True
else:
    aprovado = False

print('Este CPF é válido' if aprovado == True else 'CPF inválido') 



# Exercício Proposto: 
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""