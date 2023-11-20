class Birthdayboy():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Age(self):
        self.age+=1

boy=Birthdayboy("Vishnu",20)
print("Name of the bday boy is",boy.name)
boy.Age()
print(boy.age)
