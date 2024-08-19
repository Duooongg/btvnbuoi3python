def len_number(number:int):
    cnt =1
    while(number>10):
        cnt+=1
        number/=10
    return cnt
def sum_number(number:int):
    total = 0
    cnt = len_number(number)
    while cnt>0:
        cnt-=1
        total += number%10
        number //=10
    return total
print(len_number(12345))
print(sum_number(12345))
