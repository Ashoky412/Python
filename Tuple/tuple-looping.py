cities = ("hyd", "bng", "chennai", "Delhi")

for city in cities:
    print(city)

# using while loop
print(" ####" )
count = 0

while count < len(cities):
    print(cities[count])
    count +=1
print(" ####" )

backwards = len(cities) - 1

while backwards >= 0:
    print(cities[backwards])
    backwards -= 1



