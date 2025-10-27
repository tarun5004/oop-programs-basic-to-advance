from random import randint

class Train:
    def __init__(self, trainNo):    #constructor with one parameter
        self.trainNo = trainNo      #instance variable
        

    def book(self, fro, to):        #method to book ticket
        self.fro = fro 
        self.to = to
        self.seatNo = randint(1, 100)  #randomly generating seat number between 1 to 100
        print(f"Ticket booked from {self.fro} to {self.to} in train no: {self.trainNo} and seat number is {self.seatNo}.")
        
        
    def getstatus(self):
        print(f"Train number is {self.trainNo} running on time.")
        
    def getFare(self): 
        print(f"Ticket fare in train no: {self.trainNo} from {self.fro} to {self.to} is {randint(100, 5000)}")
        
t = Train(12345)               #creating object of class Train
t.book("Delhi", "Mumbai")   #booking ticket from Delhi to Mumbai
t.getstatus()
t.getFare()