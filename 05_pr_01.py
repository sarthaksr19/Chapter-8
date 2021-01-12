def greatest_number(num1,num2):
    if num1>num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num2} is greater than {num1}")
num1 = int(input("enter three digit number\n"))
num2 = int(input("enter three digit number\n"))

greatest_number(num1,num2)