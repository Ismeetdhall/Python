import random
hours = random.randint(35,75)

print (" Welcome to the Wages Generator",'\n')
wage=int(input("Input The Wages for an Hour"))
print ("The number of Hours are:-",hours,'\n')
if (hours>60):
    print("Wages Are: ",wage*2)
elif(40<=hours<60):
     print("Wages Are: ",wage*1.5)
else:
    print("Your Wages Will be Same as of per Hour No extra bonus is given\a")

input("\n\n\n Press enter to exit ")

