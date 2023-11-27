class Complex:
    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag
        
    def display(self):
        print(self.real, "+" ,self.imag, "i")
    
    def add(self,c1,c2):
        self.real=c1.real+c2.real
        self.imag=c1.imag+c2.imag

if __name__=="__main__":
    c1=Complex(3,4)
    c2=Complex(2,4)
    c1.display()
    c2.display()
    c3=Complex()
    c3.add(c1,c2)
    c3.display()
        
        
