
val=int(input("Enter the Interger : "))


def factorial(val):
    fact = 1
    for i in range(val,1,-1):
        fact = fact * i
    return fact

print(factorial(val))