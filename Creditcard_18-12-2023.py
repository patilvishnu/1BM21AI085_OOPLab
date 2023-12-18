class Creditcard():
    def __init__(self,account,limit,balance):
        self.account=account
        self.__limit=limit
        self.__balance=balance
    def balance(self):
        print("Balance is",self.__balance)
    def withdraw(self,amnt):
        if amnt>self.__limit:
            print("Limit exceeded!")
        if amnt>self.__balance:
            print("Balance exceeded!")
        else:
            self.__balance-=amnt
            print("Withdrawn!")
    def deposit(self,amnt):
        self._balance=amnt
        print("Deposited!")
        
c1=Creditcard("Vishnu",2000,2356)
c1.balance()
c1.withdraw(1200)
c1.withdraw(10000)
