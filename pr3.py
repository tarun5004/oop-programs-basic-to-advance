class Demo:
    a = 5                 #class variable
    
o = Demo()               #creating object of class Demo
print(o.a)               #print the class attribute becaues instance atrribute is not present

o.a = 10                 #creating instance attribute
print(o.a)               #prints the instance attribute because instance attribute has more priority than class attribute

print(Demo.a)          #prints the class attribute because we are accessing using class name  