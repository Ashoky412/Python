str=input("Enter a String : ")

rev_str = ""

for i in range(len(str)-1,-1,-1):
    rev_str +=str[i]

print(rev_str)    