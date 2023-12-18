from abc import ABC,abstractmethod
class Vehicle:
    def __init__(self,no_of_wheels):
        self.no_of_wheels=no_of_wheels
    @abstractmethod
    def start(self):
        pass

class bike(Vehicle):
    def display(self):
        print("Kickstart")
    
class car(Vehicle):
    def display(self):
        print("Selfstart")
    
class bus(Vehicle):
     def display(self):
        print("Leverstart")
        
b1=bike(2)
b1.display()
c1=car(4)
c1.display()
b1=bus(6)
b1.display()
