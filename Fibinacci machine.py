def fib():
    times = int(input("How many times would you like the process to happen?: "))
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(times - 1):
        c = a + b
        print(c)
        a = b
        b = c


print(fib())
