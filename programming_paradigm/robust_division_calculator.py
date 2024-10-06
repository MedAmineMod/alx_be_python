
def safe_divide(numerator, denominator):
   
    try : 
        float_n =  float(numerator)
        float_d =  float(denominator)
    except (ValueError):
        return ValueError("Error: Please enter numeric values only.")
    

    try :
     res  = float_n/float_d
    
    except (ZeroDivisionError)  :
        return  ZeroDivisionError("Error: Cannot divide by zero.")
    else :   
        return    f"The result of the division is {res}"

