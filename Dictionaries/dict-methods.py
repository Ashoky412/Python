dic_methods = {"Queen": "Bohemian Rhapsody",
               "Bee Gees": "Stayin' Alive",
               "U2": "One", 
               "Michael Jackson": "Billie Jean",
               "The Beatles": "Hey Jude", 
               "Bob Dylan": "Like A Rolling Stone"}
print(len(dic_methods))

for key in dic_methods.keys():
    print(key)

print(dic_methods.values())

for key, value in dic_methods.items():
    print(key, value)

print(dic_methods.get("Promise of the Real", "not available"))
