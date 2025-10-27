class calculator:                          #creating class calculator
    def __init__(self, num):               #constructor with one parameter
        self.num = num                     #instance variable 
        
    def square(self):                  #method to calculate square
            print(f"The square of {self.num} is {self.num ** 2}")    #printing square
            
    def cube(self):                    #method to calculate cube
            print(f"The cube of {self.num} is {self.num ** 3}")    #printing cube
                
    def squareroot(self):
            print(f"The square root of {self.num} is {self.num ** 0.5}")  #printing square root
                    
c = calculator(10)          #creating object of class calculator
c.square()                  #calling square method
c.cube()                    #calling cube method
c.squareroot()              #calling square root method
