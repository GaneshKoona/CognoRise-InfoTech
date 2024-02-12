import random

user_choice = int(input("enter no of sides for the dice : "))   
if user_choice==0:
    print("no outcome")
else:
    print(random.randint(1, user_choice))
    
    
