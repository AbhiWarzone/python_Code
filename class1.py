class Employee: #class is a blueprint of object
    name = "Abhi" # class attribute
    age = 29
    
    pin = 755011
a = Employee() # a is an object
a.state = "Odisha" #instance attribute
print(a.state, a.name, a.age)

#here state is instance attribute and name and age are class attributes as they directly belong to the class