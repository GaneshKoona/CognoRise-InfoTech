def addition(n1, n2):
    return n1 + n2
def subtraction(n1, n2):
    return n1 - n2
def multiplication(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2
operation = (input("Enter choice of operation : "))

n1 = float(input("Enter the First Number: "))
n2 = float(input("Enter the Second Number: "))

if operation == "add":
    print (n1, "+", n2, "=", addition(n1, n2))

elif operation == "subtract":
    print (n1, "-", n2, "=", subtraction(n1, n2)) 

elif operation == "multiply":
    print (n1, "*", n2, "=", multiplication(n1, n2)) 
    
elif operation == "divide" :
    print (n1, "/", n2, "=", division(n1, n2)) 
    
else:
    print("Invalid Input")