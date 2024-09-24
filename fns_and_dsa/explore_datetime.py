from datetime import datetime
from datetime import timedelta

def display_current_datetime () : 
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: " + current_date  )
  
    d = int(input("Enter the number of days to add to the current date: "))
    
    future_date  = datetime.now() +  timedelta(days=d)
    print(f"Future date: {future_date.date()}")
    
display_current_datetime()