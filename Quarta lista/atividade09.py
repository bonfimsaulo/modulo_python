"""
A partir do arquivo criado na atividade anterior, crie um arquivo Python atividade09.py.
Após, defina uma variável do tipo lista (list) e atribua a ela as letras 'A', 'M', 'O' e 'R', todas maiúsculas. Na
sequência, utilize o laço de repetição for e a função print para exibir cada valor da lista separadamente. No
caso da função print, após chamar a variável que será exibida, utilize o atributo end, conforme o exemplo a
seguir: print(letra, end=""). Comente a saída de dados (o que foi exibido na tela).
"""

palavra = ['A','M','O', 'R']

for letra in palavra:
    print(letra, end = ' ')