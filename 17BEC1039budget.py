print ("WELCOME TO BUDGET PROGRAM\n")
money = int(input("ENTER SALARY:"))
       
food=int(input("food expenses: "))
travelling=int(input("TRAVELLING expenses :"))
hotel=int(input("HOTEL expenses"))
sum=food+travelling+hotel
print("total expenditure: ",sum)
if(sum > money):
   print (" you are in debt.")
else:
   print("Money left : ",money-sum)
input ()
