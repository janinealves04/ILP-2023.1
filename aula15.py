


"""Exemplo de dicionario"""

agenda = {'Alex': '123',
          'Juliana': '456',
          'Luis': '789'}

print("Agenda completa:")
print(agenda)
print(agenda.keys())
print(agenda.values())
print(agenda.items())

# Adicionando novos contatos

agenda['Jonas'] = '098'
agenda['Lucas'] = '876'

print("Agenda completa atualizada:")

for chave in agenda.keys():
    print(chave, end='/')

for valor in agenda.values():
    print(chave, end='/')
print()
