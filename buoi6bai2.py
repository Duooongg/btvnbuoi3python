def transposition_matrix(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transposed.append(row)
    return transposed
n = int(input("Số hàng: "))
m = int(input("Số cột: "))
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        k = input(f"Phần tử tại vị trí ({i + 1},{j + 1}): ")
        row.append(k)
    matrix.append(row)
print("Ma trận ban đầu:")
for row in matrix:
    print(row)
transposed_matrix = transposition_matrix(matrix)
print("Ma trận chuyển vị:")
for row in transposed_matrix:
    print(row)