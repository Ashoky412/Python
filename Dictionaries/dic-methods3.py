internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

print(internet_celebrities)

internet_celebrities.update({"motor": "honda"})

print(internet_celebrities)

internet_celebrities.update(another_one)

print(internet_celebrities)

var = internet_celebrities.copy()
print(var)

internet_celebrities.clear()
print(internet_celebrities)
print(var)

