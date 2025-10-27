class programmer:    #class programmer
    company = "Microsoft"
    def __init__(self, name, salary, pin):    #putting constructor
        self.name = name                      #creating instance variable
        self.salary = salary
        self.pin = pin
        
p = programmer("Tarun", 25000, 250408)   #creating object of class programmer
print(p.name, p.salary, p.pin)

r = programmer("Riya", 25000, 250408)   #creating second object of class programmer
print(r.name, r.salary, r.pin)