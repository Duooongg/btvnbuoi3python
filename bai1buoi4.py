tuple_1 = ("0","1","2","3","4","5","6","7","8","9")
print(tuple_1)
tuple_1 = list(tuple_1)
for i in range(0,len(tuple_1)):
    tuple_1[i] = int(tuple_1[i])
tuple_1 = tuple(tuple_1)    
print(tuple_1) 