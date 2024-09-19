ent_val=int(input(" Enter the integer :"))
int_val = ent_val

summed = 0

while ent_val > 0:
    summed = summed + ent_val
    ent_val = ent_val - 1

print("Entered interger is " + str(int_val))
print("result of entered Value :"+ str(summed))    
