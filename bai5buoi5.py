from itertools import combinations

n = int(input("nhap so luong ptu cua mang: n =  "))
a = []
print("nhập mảng xâu kí tự: ")
for i in range(0,n):
    c = str(input())
    a.append(c)

for i in range(1, n+1):
    for tuple_C in combinations(a,i):
        print(tuple_C, end = " ")
        if all(c.isdigit() for c in tuple_C) == True:
            print("la dang so")
        else:
            print("khong phai dang so")