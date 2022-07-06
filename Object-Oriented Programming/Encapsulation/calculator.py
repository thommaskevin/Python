class Calculator:

    def calculate(self, op, num1, num2):
        if op == '+':
            return self.__add(num1, num2)
        elif op == '-':
            return self.__minus(num1, num2)
        else:
            return 'Operação inválida!'

    def __add(self, num1, num2):
        return num1 + num2
        
    def __minus(self, num1, num2):
        return num1 - num2 
    


cal = Calculator()
result = cal.calculate('*', 1, 2)
print(result)