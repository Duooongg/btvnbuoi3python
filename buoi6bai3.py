def calculate(*args,operation):
    result = 0
    if operation =="add":
        for i in args:
            result +=i
    elif operation =="multiply":
        for i in args:
            result *=i
    elif operation =="max":
        result =  max(args)
    elif operation=="min":
        result = min(args)
    return result

a = calculate(1,2,3,4,operation="min")
print(a)