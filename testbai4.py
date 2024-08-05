s = input()
lst= []
for char in s:
    if char == " ":
        continue
    lst.append(char)
print(set(list(lst)))