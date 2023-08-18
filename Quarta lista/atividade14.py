"""
Repita os procedimentos da atividade anterior em um arquivo Python atividade14.py. Dessa vez, utilize o
algoritmo anterior para contar a quantidade de consoantes.
"""
palavra = input('Digite uma palavra qualquer:').lower()
qtd_vogais = 0
qtd_consoantes = 0

for letra in palavra:
    
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        qtd_vogais += 1
    else:
        qtd_consoantes += 1
    
print(f'A palavra {palavra} tem {qtd_consoantes} consoantes.')

##################################################

palavra = input('Digite uma palavra qualquer: ').lower()
letras = []

for letra in palavra:
    letras.append(letra)
    vogais = letras.count('a') + letras.count('e') + letras.count('i') + letras.count('o') + letras.count('u')

consoante = len(letras) - vogais 
print(f'A palavra {palavra} tem {consoante} consoantes')




