"""
Repita os procedimentos da atividade anterior em um arquivo Python atividade15.py. Após, peça que o
usuário informe uma frase qualquer e armazene o valor lido em uma variável. Na sequência, utilize o laço for
para verificar quantos espaços há na frase em questão. Ao final, exiba ao usuário a seguinte mensagem:
print(f"A frase {frase} tem {quantidade} espaços.")
"""

frase = input('Escreva uma frase qualquer: ').lower()
qtd_espacos = 0

for caractere in frase:
    
    if caractere == ' ':
        qtd_espacos += 1

print(f' A frase "{frase}" tem {qtd_espacos} espaços')