def criptografia(msg, chave):
    s = ''
    for i in msg:
        s = s + chr(ord(i) + chave)
    return s
def descriptografa(msg, chave):
    s = ''
    for i in msg:
        s = s + chr(ord(i)- chave)
    return s
 
x = criptografia ("Alibaba!", 1)
print(x)

res = descriptografa (x,1)
print(res)

