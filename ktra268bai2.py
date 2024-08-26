k = int(input("nhap k"))
n=0
for i in range(1, 500):
    sum =0
    a=i
    while i>0:
        sum+=i%10
        i= i//10
    if(sum ==10):
        n +=1
    if(n==k):
        print(a)
        break;

    

