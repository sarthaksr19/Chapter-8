def inches_to_cm(n):
    cm = float(2.54 * n)
    return cm

n = float(input("enter inches\n"))
print(n,"inches is equal to",inches_to_cm(n),"cm's")
