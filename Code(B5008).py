def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+ recur_fibo(n-2))
    
nterms =15

if nterms<=0:
    print("Enter a positive number")
else:
    print("Fibonacci sequence is: ")
    for i in range(nterms):
        print(recur_fibo(i))