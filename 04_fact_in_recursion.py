def factorial_recursive(n):
    if n == 1 or n == 0:  #base function
        return 1
    return n * factorial_recursive(n-1)
n = int(input("enter the number you want factorial\n"))
fact = factorial_recursive(n)
print(fact)