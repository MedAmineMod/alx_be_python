

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

op = input("Choose the operation (+, -, *, /): ")

num1 = float(num1)
num2 = float(num2)


match op:
    case  "+" : print(f"The result is {num1 + num2}.")
    case  "-" : print(f"The result is {num1 - num2}.")  
    case  "*" : print(f"The result is {num1 * num2}.")  
    case  "/" : 
        if  num2 == 0  :
            print("Cannot divide by zero.")
        else :    
            print(f"The result is {num1 / num2}.")  