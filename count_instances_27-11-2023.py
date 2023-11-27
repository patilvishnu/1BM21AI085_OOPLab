class Student:
    counter=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.counter+=1
        
    def display(self):
        print(self.name)
        print(self.marks)
    
    @classmethod
    def obj_count(cls):
        print(Student.counter)
    
if __name__=="__main__":
    s1=Student('Vishnu',67)
    s2=Student("Prahladh",90)
    s1.display()
    Student.obj_count()
