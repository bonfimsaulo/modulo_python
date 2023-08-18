"""
A partir do arquivo criado na atividade anterior, crie um arquivo Python atividade12.py. Após, defina uma
variável do tipo lista (list) e atribua a ela cinco notas, sendo: 9.9, 10, 7.1, 7.8. Em seguida, utilize o laço de
repetição for para somar essas notas e, ao final, exibir ao usuário a média ponderada. Considere os seguintes
pesos para cada nota, respectivamente: 4, 2, 3, 1.
"""

notas = [9.9 * 4, 10 * 2, 7.1 * 3, 7.8 * 1]
soma = 0
soma_pesos = 4 + 2 + 3 + 1
for nota in notas:
    soma += nota

print(f'A média ponderada obtida foi de {soma/soma_pesos}')

#####

notas = []
pesos = []
soma_notas = 0
soma_pesos = 0

for nota in range(4):
    nota = float(input(f'Digite a {nota + 1}ª nota: '))
    notas.append(nota)
    peso = int(input('Informe o peso da nota: '))
    pesos.append(peso)
       
    soma_notas += nota * peso
    soma_pesos += peso
    media = round((soma_notas/soma_pesos), 2)

print('Notas:', notas)
print(f'A média ponderada obtida foi de {media}')