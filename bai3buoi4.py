set_A = {1,15,18,21,23}
set_B = {6,66,78}

point_happy = 0

my_set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

happy = my_set.intersection(set_A)
unhappy = my_set.intersection(set_B)

point_happy = point_happy + (len(happy) - len(unhappy))
print("mức độ happy: ", point_happy)
if point_happy > 0:
    print("happy")
elif point_happy == 0:
    print("normal")
else:
    print("unhappy")