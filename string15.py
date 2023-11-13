str11=input("ENTER THE STRING :")
str12=input("ENTER THE STRING :")
cnt1=0
cnt2=0
for i in str11:
    cnt1+=1
for j in str12:
    cnt2+=1
if(cnt1<cnt2):
    print(str12,"is bigger than ",str11)
elif(cnt1>cnt2):
    print(str11,"is bigger than ",str12) 
else:
    print(str11,"is equal to ",str12)               