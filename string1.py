st1=input("ENTER THE STRING :")
str2=" "
for i in range(0,len(st1)):
    if(st1[i]=='a')or(st1[i]=='A'):
        str2+="$"
    else:
        str2+=st1[i]
print("modified string is :",str2)            
