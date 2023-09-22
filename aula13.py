
"""Exemplo 01 """
notas = [6,7,5, 8,9] 
soma = 0
x = 0

while x < 5 :
    soma += notas[x]
    x = x + 1
print ("Media: %5.2f" % (soma/x))


"""exemplo 2 """
cavaleiros = ['guerra', 'fome', 'peste']
x = 'peste' in cavaleiros
print (x)


"""Exemplo 03"""
lista = [[0]*5]*5
print (lista)

"""em tabela"""

for linha in lista:
    for x in linha :
        print (x, end=" ")
    print()