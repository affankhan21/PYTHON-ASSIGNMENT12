data=input("ENTER STRING TO REVERSE :")
rev=""
l=len(data)
for i in range(l-1,-1,-1):
    rev=rev+data[i]
data=rev    
print("REVERESE OF STRING IS  :",data)    