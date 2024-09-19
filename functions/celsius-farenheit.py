celsius=int(input("Enter the celsius temp : "))

def farenheit_temp(celsius):
    return (18 * celsius + 320) / 10

print(" The farenheit of  "+ str(celsius) + " degree celsius is " + str(farenheit_temp(celsius)) + " ." )