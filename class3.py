class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
p = Programmer("Abhi",1200000, 755011)

print(p.name, p.salary, p.pin)