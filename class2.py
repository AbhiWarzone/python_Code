class Employee: #class is a blueprint of object
    name = "Abhi" # class attribute
    age = 29
    
    def getinfo(self):
        print(f"The state is {self.state}. The age is {self.age}")
    def greet(self):
        print("Hi Welcome")
    def __init__(self):                             #Dunder method which is automtically called 
        print("class is an blueprint of object")
        
    @staticmethod
    def hello():
        print("Hello Abhi")

    pin = 755011
a = Employee() # a is an object
a.state = "Odisha" #instance attribute
print(a.state, a.name, a.age)
a.getinfo()
#Employee.getinfo(a)
a.greet()
a.hello()