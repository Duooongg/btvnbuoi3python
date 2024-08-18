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
#5
def format_phone_number(phone_number):
    digits =''.join(filter(str.isdigit,phone_number))

    if len(digits) !=10 or not digits.startswith('0'):
        return "Ivalid phone number"
    return "+84" + digits[1:]
print(format_phone_number("0923-432-654"))