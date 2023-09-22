def fibbonacci(x):
    seq = [1, 1]
    for i in range(2, x):
        soma = seq[i-2] + seq[i-1]
        seq.append(soma)
        return seq
    print(fibbonacci(10))


# ex.02 beecrowd
linha = input().split(" ")
linha_int = []

for valor in linha:
    linha_int.append(int(valor))


linha_ord = sorted(linha_int)

for i in linha_ord:
    print(i)

for i in linha:
    print(i)