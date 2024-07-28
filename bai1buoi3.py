n = int(input("Nhap so phan tu cua list: "))
lst = []
for i in range(n):
    lst.append(int(input()))
print("lst =",lst)

import math
x = int(input("Nhap x = "))
a = lst.count(x)
print("So lan xuat hien", x, "trong list la: ", a)

lst[2:8] =[8, 5, 4, 0, 1, 3]
print("List sau khi thay the la: lst =", lst)

print("So lon nhat trong list la: ",max(lst))
print("So nho nhat trong list la: ",min(lst))

y = int(input("Nhap y = "))
lst.insert(0,y)
print("lst =",lst)

if lst.sort():
    print("TĂNG")
if lst.sort(reverse=True):
    print("GIẢM")
else:
    print("NO")

new_list = []
sum = 0

for i in range(n):
    sum += lst[i]
    new_list.append(sum)
print("Danh sách mới:", new_list)

lst2 = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
lst2.sort()
print("lst2 =", lst2)
for i in range(len(lst2)):
    lst2[i] = abs(lst2[i])
lst2.sort()
print("lst2 =", lst2)