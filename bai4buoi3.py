ho_ten = input("Nhập họ tên: ")
ho_ten = ho_ten.strip()
ho_ten_chuan = ""
i = 0

while i < len(ho_ten):
    if ho_ten[i] != ' ':
        ho_ten_chuan += ho_ten[i]
    elif ho_ten_chuan[-1] != ' ':
        ho_ten_chuan += ' '
    i += 1

ho_ten_chuan = ho_ten_chuan.lower()
result = ""
new_word = True

for char in ho_ten_chuan:
    if new_word:
        result += char.upper()
        new_word = False
    else:
        result += char
    if char == ' ':
        new_word = True

print(result)