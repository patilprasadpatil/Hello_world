def fibo(n):
    a = 0
    b = 1
    if a==1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
x = int(input("Enter a Number: "))
fibo(x)
