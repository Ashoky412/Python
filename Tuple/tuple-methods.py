nested = (1, 2, 3, (1, 2, 3), (4, 5, 6))

print(nested[2]) # 3
print(nested[4][1]) # 5

var1 = ( 1, 7, 2, 7, 1, 2, 1, 2, 7, 4, 5, 7, 7, 2, 7)
print(var1.count(7)) # 6
print(var1.count(1)) # 3
print(var1.count(2)) # 4

print(" ###### ")
print(var1.index(4))   # 9
print(var1.index(5))   # 10




