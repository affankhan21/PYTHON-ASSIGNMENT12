str11=input("ENTER THE STRING  :")
str12=input("ENTER THE STRING  :")

s1=str11.lower()
s2=str12.lower()
if(len(s1))==(len(s2)):
    s1=sorted(s1)
    print(s1)
    s2=sorted(s2)
    print(s2)
    if(s1 == s2):
        print(" are anagram.")
    else:
        print(" are not anagram.")    
else:
        print(" are not anagram.")            