def Dogrula(uzantı,mailadresi):
    h='@'
    if uzantı<1 or uzantı>3:
       # print("Lütfen belirtilen aralıkta bir uzunluk girin: ")
        return False
    else:
        if h in mailadresi:
            indeks=mailadresi.index(h)
            ayır1=mailadresi.split("@")
            ayır2=ayır1[1].split(".")
           
            if uzantı==len(ayır2):
                    return True
               
            else:
               return False
                 
        else:
            return False
  
uzantı=int(input("Uzantının uzunluğunu giriniz (1 2 3 den birisi.): "))
mailadresi=str(input("Lütfen mail adresinizi girin: "))
 
if Dogrula(uzantı,mailadresi) == True:
     print("Mail adresiniz doğrudur.")    
else:
     print("Mail adresiniz yanlıştır.")


