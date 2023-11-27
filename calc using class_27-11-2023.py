class Calculator:
    def __init__(self,version):
        self.version=version
        
    def display(self):
        print(self.version)
        
    @staticmethod
    def add(n1,n2):
        print(n1+n2)
    
if __name__=='__main__':
        c1=Calculator(2)
        c2=Calculator(5)
        c1.display()
        Calculator.add(10,20)     
