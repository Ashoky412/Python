val_num=range(1,50)

fizz = "fizz"
buzz = "buzz"
fizzbuzz ="fizzbuzz"

for num in val_num:
    if num % 3 == 0 and num % 5 == 0:
        print(fizzbuzz)
    elif num % 3 == 0 and num % 5 != 0:
        print(fizz)
    elif num % 3 != 0 and num % 5 == 0:
        print(buzz)
    else:
        print(num)     
