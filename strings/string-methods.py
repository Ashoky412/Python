var ="A Song of Ice and Fire"

print(var.isupper())
print(var.islower())
print(var.upper())
print(var.lower())
print(var.istitle())

var2 = var.title()
print(var2)

print(var.startswith("A"))
print(var.endswith("e"))
words=var.split()
print(words)
print(" ".join(words))
print(" ".join(words).isalpha())