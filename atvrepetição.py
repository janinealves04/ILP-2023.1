#variaveis
maior_media = -1 #proque 01?
menor_media = 10
m_nome = ""
m_n1, m_n2= 0,0 #é a formatação?
me_n1, me_n2 = 0,0
me_nome = ""
#ler o numero de alunos
quant_alunos = int(input("Quantidade de alunos:"))

#Repetição
for i in range(quant_alunos):
    nome = input("digite nome do aluno:")
    n1 = input("digite a segunda nota:")
    n2 = input("digite a segunda nota:")
    media =(n1 +n2)/2
    if (media > maior_media):
        maior_media = media
        m_n1, m_n2 = n1,n2
        m_nome = nome 
    if (media < menor_media):
        menor_media = media
        me_n1, me_n2 = n1,n2
        me_nome = nome 
print ("O ALUNO(A)",m_nome, "tem a maior médiia")
print("A maior média é:",maior_media)
print("Sua menor média é:",menor_media)
print("Suas notas foram:",m_n1, "e", m_n2)


