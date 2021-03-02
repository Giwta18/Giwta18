x=int(input("Dwse to mhkos tou orthogwniou:"))
y=int(input("Dwse to platos tou orthogwniou:"))
lists=[[] for i in range(x+1)]
matrix1=[["s" for j in range(y)]for i in range(x//2)]
matrix2=[["o" for j in range(y)] for i in range(x-(x//2))]
import random
matrix3=matrix1 + matrix2
random.shuffle(matrix3)
[random.shuffle(sublist) for sublist in matrix3]
print(matrix3)
