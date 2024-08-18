check = lambda a,b: a if ord(a)>ord(b) else b
a = input("a: ")
b = input("b: ")
print(check(a,b))