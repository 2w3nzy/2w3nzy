from random import choice,choice,choices
sayilar=(1,2,3,4,5,6,7,8,9,0,)
sifre=str(input("Ara0a1ak  21fr3 ?¿"))
sifres=""
adim=0
while True:
 print("Aranıyor?¿",sifres)
 
 if sifre==sifres:
  break
  
 else:
  sifres=""
  for i in range(4):
   sifres+=str(choice(sayilar))
   adim+=1
   
print("|3u1un6u¤",sifre,)