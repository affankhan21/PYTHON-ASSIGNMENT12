n=input("ENTER THE STRING :")
word=input("ENTER THE WORD :")
a=[]
count=0
a=n.split(" ")
for i in range(0,len(a)):
    if(word==a[i]):
        count+=1
print("COUNT OF THE WORD :",count)        