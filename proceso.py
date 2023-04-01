



c=int(input("Digite el valor de n: "))

n=0
d=2*c

while (c<d):
    c = c + 0.05 * c
    n = n + 1
    print("Mes: "+str(n))
    print("Capital: "+str(c))
  
print("La suma es: "+str(n))