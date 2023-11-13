
str11=input("ENTER STRING :")
n =int(input("ENTER THE NUMBER TO REMOVE FROM STRING :"))
str12=""
for i in range(0,len(str11)):
    if(i!=n):
        str12+=str11[i]
print("MODIFIED STRING IS :")
print(str12)        