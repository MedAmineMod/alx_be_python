

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

op = input("Choose the operation (+, -, *, /): ")

num1 = float(num1)
num2 = float(num2)

if op == "+" : print(f"The result is {num1 + num2}.")  
elif op == "-" : print(f"The result is {num1 - num2}.")  
elif op == "*" : print(f"The result is {num1 * num2}.")  
elif op == "/" : 
    if num1 > num2 :
        print("Cannot divide by zero.")
    else :    
        print(f"The result is {num1 / num2}.")  