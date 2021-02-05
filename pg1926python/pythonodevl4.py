sayıdizisi=[]
kactane= str(input("Araya virgül bırakarak değerleri girin. Örnk: [1,2,3,4]:   "))
sayıdizisi=kactane.split(",")
sayıdizisi=list(map(int, sayıdizisi))
tekler=[]

for a in sayıdizisi:
    if(a%2==1):
        tekler.append(a)
      

print(max(tekler))



