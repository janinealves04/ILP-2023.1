def primo(x):
       for i in range (2,int(x/2)+1):
        #print(o numero ", x , é divisivel por ", i, "?")
            if (x%i == 0):
            #print ("o numero, x é divisivel por i "!")
            return False
    return True 

for z in range (2, 1001):
       if (primo(z)):
              print(z)

#exemplo 02
 def fibo