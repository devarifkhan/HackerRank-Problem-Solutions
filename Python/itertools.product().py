from itertools import product
A=input().split()
A=list(map(int,A))
B=input().split()
B=list(map(int,B))
for i in product(A,B):
    print(i,end=" ")


# for i in product(list[0],list[1]):
#     print(i,end=' ')
