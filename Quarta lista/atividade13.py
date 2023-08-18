"""
Crie um arquivo Python atividade13.py. Após, peça que o usuário informe uma palavra qualquer e armazene
o valor lido em uma variável. Na sequência, utilize o laço for para verificar quantas vogais têm na palavra em
questão. Ao final, exiba ao usuário a seguinte mensagem: print(f"A palavra {palavra} tem {quantidade}
vogais.")
"""

palavra = input('Digite uma palavra qualquer:').lower()
qtd_vogais = 0

for letra in palavra:
    
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        qtd_vogais += 1
    
print(f'A palavra {palavra} tem {qtd_vogais} vogais.')

######################################################

palavra = input('Digite uma palavra qualquer: ').lower()
letras = []

for letra in palavra:
    letras.append(letra)
    vogais = letras.count('a') + letras.count('e') + letras.count('i') + letras.count('o') + letras.count('u')

print(letras)
print(f'A palavra {palavra} tem {vogais} vogais')