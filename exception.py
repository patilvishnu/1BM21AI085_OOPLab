6 a)
class WrongAge(Exception):
    def __init__(self, message="Age should be greater than or equal to 0"):
        self.message = message
        super().__init__(self.message)


class AgeInvalid(Exception):
    def __init__(self, message="Son's age should be less than Father's age"):
        self.message = message
        super().__init__(self.message)


class Father:
    def __init__(self, age):
        if age < 0:
            raise WrongAge()
        self.age = age


class Son(Father):
    def __init__(self, father_age, son_age):
        super().__init__(father_age) 
        if son_age >= father_age:
            raise AgeInvalid()
        self.son_age = son_age


try:
    father_age = int(input("Enter Father's age: "))
    son_age = int(input("Enter Son's age: "))
       
    father = Father(father_age)
    son = Son(father_age, son_age)
    
 

    print("Father's age:", father.age)
    print("Son's age:", son.son_age)

except WrongAge as wa:
    print("Error:", wa)

except AgeInvalid as ai:
    print("Error:", ai)

except ValueError:
    print("Error: Please enter a valid integer for age.")

6 b)

class FormulaError(Exception):
    pass

def calculate(formula):
    try:
        parts = formula.split()
        if len(parts) != 3:
            raise FormulaError("Invalid formula. Must consist of a number, an operator (+ or -), and another number.")
          
        num1 = float(parts[0])
        num2 = float(parts[2])
        operator = parts[1]
        if operator not in ['+', '-']:
            raise FormulaError("Invalid operator. Operator must be + or -.")

       
        result = num1 + num2 if operator == '+' else num1 - num2

        print("Result:", result)

    except ValueError:
        raise FormulaError("Invalid number format. Please enter valid numeric values.")


while True:
    try:
        
        user_input = input("Enter a formula (e.g., 1 + 1) or type 'quit' to exit: ")

        
        if user_input.lower() == 'quit':
            break

      
        calculate(user_input)

    except FormulaError as fe:
        print("Error:", fe)
