str1=input("ENTER THE STRING :")

print(len(str1))
cnt=0
for i in str1:
    if i in "aeiou" or i in "AEIOU":
        cnt+=1
print(str1)        
print("THE COUNT OF VOWELS ARE :",cnt)        