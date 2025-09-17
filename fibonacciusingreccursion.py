def fibonacci(n):
    '''nth term in fibonacci series'''
    if n<=1:
        return n
    eturn fibonacci(n-1)+fibonacci(n-2)

n= int(input("Enter n:"))
print(f"{n}th term in fibonacci series is:",fibonacci(n))
