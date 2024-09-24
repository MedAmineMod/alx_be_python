FAHRENHEIT_TO_CELSIUS_FACTOR  = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR  = 9/5



def convert_to_celsius (fahrenheit) :
    
    calc =    (fahrenheit - 32 )  * FAHRENHEIT_TO_CELSIUS_FACTOR
    
    print(f"{fahrenheit}°F is {calc}°C")


def convert_to_fahrenheit (celsius) :
     
    calc =    (celsius  * CELSIUS_TO_FAHRENHEIT_FACTOR )  + 32
    
    print(f"{celsius}°C is {calc}°F")

    
    
 
 

temp = input("Enter the temperature to convert: " )

try:
    temp = float(temp) 

    type = input("Is this temperature in Celsius or Fahrenheit? (C/F): " )

    if type.upper() == "F" : 
         convert_to_celsius(temp)
    else :
        convert_to_fahrenheit(temp)

except :
    print("Invalid temperature. Please enter a numeric value.")

