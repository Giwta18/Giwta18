p = int(input("Dwse to n:"))
sum=0
for i in range(1, 21):
    a = int(input("Dwse to a:"))
    if (a^p % p) == (a % p):
        sum+=1

if sum==20:
    print("Ο n όρος της ακολουθίας fibonacci είναι πρώτος")
else:
    print("Ο n όρος της ακολουθίας fibonacci δεν είναι πρώτος")
