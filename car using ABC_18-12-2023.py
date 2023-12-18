from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
    def wheels(self):
        print("4 wheels")
        
class Tata(Car):
    def mileage(self):
        print("tata mileage is 31")
        
class Maruti(Car):
    def mileage(self):
        print("maruti mileage is 39")
        
class Ford(Car):
    def mileage(self):
        print("Ford mileage is 35")
        
t=Tata()
m=Maruti()
f=Ford()
t.mileage()
f.mileage()
m.mileage()

