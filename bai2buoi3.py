a = list(map(int, input("Nhap cac phan tu cua list a: ").split()))
k = len(a)
n = int(input("Nhap so dong n: "))
m = int(input("Nhap so cot m: "))

if n * m > k:
    print("NO")
else:
    matrix = []
    index = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[index])
            index += 1
        matrix.append(row)
    for row in matrix:
        print(row)