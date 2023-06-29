import random

nove_digitos_cpf = ''

for digitos in range(9):
    nove_digitos_cpf += str(random.randint(0, 9))


auxiliar = 10 #usa-se 10 digitos como auxiliar no primeiro dígito

soma = 0
for digito in nove_digitos_cpf: #looping para realizar multiplicação e soma do resultado para lista
    soma += int(digito) * auxiliar
    auxiliar -= 1

digito_1 = (soma * 10) % 11 #digito 1 receberá o restante da divisão por 11

digito_1 = digito_1 if digito_1 <= 9 else 0 #condicional

nove_digitos_cpf += str(digito_1)

dez_digitos = nove_digitos_cpf[:10] #início do cálculo do segundo dígito adicionando o primeiro

auxiliar_2 = 11 #usa-se 11 dígitos como auxiliar no segundo dígito

soma2 = 0
for digito in dez_digitos: #looping para realizar multiplicação e soma do resultado para lista
    soma2 += int(digito) * auxiliar_2
    auxiliar_2 = auxiliar_2 - 1

digito_2 = (soma2 * 10) % 11

digito_2 = digito_2 if digito_2 <= 9 else 0

nove_digitos_cpf += str(digito_2)

print(nove_digitos_cpf)