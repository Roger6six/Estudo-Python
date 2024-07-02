# uso da f strings
nome = 'Junior'
altura = 1.77
peso = 90.0
imc = peso / (altura ** 2)
linha_1 = f'{nome} tem {altura} de altura'
linha_2 = f'pesa {peso} e o seu IMC é {imc:.2f}'

print(linha_1)
print(linha_2)
