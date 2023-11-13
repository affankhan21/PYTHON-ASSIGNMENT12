str2=input("ENTER THE STRING :")
res=" "
for i in range(len(str2)):
    if(i+1)%2==0:
       res=res+str2[i]
print("THE MODIFIED STRING IS :",res)   
