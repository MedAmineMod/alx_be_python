from datetime import datetime
from datetime import timedelta

def display_current_datetime () : 
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: " + current_date  )
  
    d = int(input("Enter the number of days to add to the current date: "))
    
    calculate_future_date  = datetime.now() +  timedelta(days=d)
    
    print(f"Future date: {calculate_future_date.date().strftime("%Y-%m-%d")}")
    
display_current_datetime()