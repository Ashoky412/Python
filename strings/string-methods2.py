the_string="North Dakota"
print(the_string.rjust(17))
print(the_string.ljust(17,"*"))
center_plus=the_string.center(16,"+")
print(center_plus)
print(center_plus.lstrip("North"))
print(center_plus.rstrip("+"))
print(center_plus.strip("+"))
print(the_string.replace("North","South"))


