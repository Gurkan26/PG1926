sayıdizisi=[]
kactane= int(input("Kaç adet sayı gireceksin: "))
i=0
j=0
tasıyıcı=0
while i<kactane:
    sayılar= input("Sayıyı girin: ")
    sayıdizisi.append(sayılar)
    i+=1
while True:
 if "0" in sayıdizisi:
     index1= sayıdizisi.index("0")
     print(index1)
     tasıyıcı=sayıdizisi.index(0)
     sayıdizisi.index(0)=sayıdizisi.index(index1)

 break
for a in sayıdizisi:
    print(a+",")
    