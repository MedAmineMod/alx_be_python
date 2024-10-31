import math 

class Shape:

    def area(self):
        return  NotImplementedError

class Rectangle(Shape):
    def __init__(self , width , length):
        
        self.length =  length 
        self.width = width
        
    def area(self):
        return  self.width * self.length

class Circle(Shape):
    
    def __init__(self , radius):
         
        self.radius = radius
    
    def area(self):
        return  math.pi * self.radius ** 2
        


earth =  Circle(23)

print(earth.area())
