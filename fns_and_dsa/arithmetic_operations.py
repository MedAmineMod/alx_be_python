def perform_operation(num1,num2,operation): 
    
    match operation : 
        case "add" :
            return num1 + num2
        case  "subtract": 
            return num1 - num2
        case  "multiply" :
            return num1 * num2
        case  "devide" :
            if(num2 != 0) :
                return num1 / num2
        case _:
            print("Not allowed operation")
            
        
    
    
