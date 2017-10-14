def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

def fibo(n) :
    if n==0 :
        return 0
    if n==1 :
        return 1
    else :
        return fibo(n-1)+fibo(n-2)

print fibo(5)
print F(8)


a=0
b=1

for i in range (0,9) :
    if i == 0 :
        print a
    elif i == 1 :
        print b
    else :
        print a+b
        a,b=b,a+b
        
