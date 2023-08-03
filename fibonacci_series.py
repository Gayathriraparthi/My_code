def fibo(n):
    fib = [0,1]
    a = 0
    b = 1
    for i in range (1,n-1):
        c = a+b
        fib.append(c)

        a = b
        b = c
        
    return (fib)

print(fibo(9))



