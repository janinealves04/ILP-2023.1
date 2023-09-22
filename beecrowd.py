linha = input().split(" ")
linha_int = []

for valor in linha:
    linha_int.append(int(valor))


linha_ord = sorted(linha_int)

for i in linha_ord:
    print(i)

for i in linha:
    print(i)

#Ler um valor N. Calcular e escrever seu respectivo fatorial.
# Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

