def f(n):
    
    if (n == 0) :
        print('honey')
        return
    
    for i in range(0, n):
        f(n-1)

f(4)