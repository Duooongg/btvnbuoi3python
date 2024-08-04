
tap_A = {1,5,2,7,6,3,9,4,8}
tap_B = {11,20,4,3,12,13,9,16,15}

print("tap 1: ", tap_A)
print("tap 2: ", tap_B)

tap_AB = tap_A.intersection(tap_B)

tap_A_not_B = tap_A.difference(tap_B)

if len(tap_AB) != 0:
    print(f"có {len(tap_AB)} sinh vien đăng ký học tại cả hai bàn ")
    l = list(tap_AB)
    print("danh sách tổng hợp msv của các sinh viên đã đăng ký của cả hai bàn: ")
    for i in range(0,len(l)):
        print(l[i],end = " ")
    print("\n")
    l_1 = list(tap_A_not_B)
    print("danh sách tổng hợp msv của các sinh viên đã đăng ký của cả hai bàn: ")
    for i in range(0,len(l_1)):
        print(l_1[i],end = " ")
else:
    print("khong có sinh vien đăng ký học tại cả hai bàn ")
    l_1 = list(tap_A_not_B)
    print("danh sách tổng hợp msv của các sinh viên đã đăng ký của cả hai bàn: ")
    for i in range(0,len(l_1)):
        print(l_1[i],end = " ")