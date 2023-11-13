digits="0123456789"
lower="abcdefghijklmnopqrstuvwxyz"
str13=input("ENTER THE STRING :")
idig=0
ilower=0
for i in str13:
    if i in digits:
        idig+=1
    elif i in lower:
        ilower+=1
print("NUMBER  OF DIGITS ARE      :",idig)
print("NUMBER OF LOWER CASE ARE   :",ilower)            