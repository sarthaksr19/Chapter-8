def sum_natural_recursive(n):
    wrong_number = False
    if n == 1:   #base case
        return 1
    elif n<1:
        return None

    return n + sum_natural_recursive(n-1)

n = int(input("enter the number you want sum\n"))
print(sum_natural_recursive(n))