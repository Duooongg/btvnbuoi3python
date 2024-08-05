n= int(input())
svien = []
for _ in range(n):
    data = input("nhap ten va diem ").split()
    name = data[0]
    score = float(data[1])
    svien.append((name, score))
dkien = int(input("nhap diem can thoa man "))
for name, score in svien:
    if score == dkien:
        print(name)

