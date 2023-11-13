str2=input("ENTER THE STRING :")
char=0
word=1
for i in str2:
    char=char+1
    if(i == " "):
        word =word+1
print("NUMBER OF WORDS ",word)
print("NUMBER OF CHARACTERS ",char)        