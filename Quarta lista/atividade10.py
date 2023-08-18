"""
Crie um arquivo Python atividade10.py. Após, defina uma variável do tipo lista (list) e atribua a ela cinco
palavras, sendo: "limão", "laranja", "maracujá", "abacaxi" e "mexerica". Depois, peça ao usuário que informe
uma fruta, e atribua o valor lido a uma variável fruta. Finalmente, utilize a condicional if e verifique se a fruta
informada pelo usuário faz parte da lista de frutas que você definiu anteriormente. Se verdadeiro, exiba o
nome da fruta; caso contrário, informe ao usuário: "A fruta informada não está na lista". Dica: utilize o operador
relacional in para resolver esse exercício.
"""

cesta = ['limão', 'laranja', 'maracujá', 'abacaxi', 'mexerica']

fruta = input('Informe uma fruta: ')

if fruta in cesta:
    print(f'{fruta} está na cesta')
else:
    print(f'{fruta} não está na cesta')