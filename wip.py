print("podaj ciąg znaków")
CIAG = input()
SAMOG = 0
for litera in CIAG:
    if litera in ('e','y','u','i','o','a'):
        SAMOG += 1
print("w podanym ciągu jest",SAMOG,"samogłosek")
#bez polskich znaków
