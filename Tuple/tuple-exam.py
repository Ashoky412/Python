var1 =("a", "b", "c", "d")
var2 =(1, 3, 5, 7, 9)
var3=(1, 2, 4, (1, 2, 3))
var4=(1, "a", 3.14, [1, 2])

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))


var5=tuple("anbcjbdcb")
print(type(var5))
print(var5)


#tuples are immutable

var6=(1, 3, 5, 7, 9, 11, 4, 2, 8)
print(var6)
# var6[4]=8   # TypeError: 'tuple' object does not support item assignment
print(var6)


# tuples optimizes memory when compared with ## lists ##

var7 = (1, 2, 3)
var8 = [1, 2, 3]

print(var7.__sizeof__()) # 48
print(var8.__sizeof__()) # 72