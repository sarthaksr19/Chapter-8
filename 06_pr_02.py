## celsius to farhenheit conversion.

def celsius_to_farhenheit(c):
    farh = float(c*1.8) + 32
    return farh
c = float(input("enter the celsius\n"))
print(celsius_to_farhenheit(c),"farhenheit")