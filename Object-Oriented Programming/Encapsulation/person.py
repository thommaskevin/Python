class Person:
    def __init__(self, name, years_old, register):
        self.name = name
        self.years_old = years_old
        self.__register = register # '__' This attribute is Encapsulated


    def running(self):
        print('The person is running')

    '''
        Use '__' for encapsulate this method
    '''    
    def __show_register(self): # 
        print(self.__register)

    '''
         This method use Encapsulation (private method and attribute)
    '''
    def drinking(self, drink):
        if drink == 'beer':
            self.__show_register()
        print('Drinking {}'.format(drink))

person01 = Person('John', 23, '123456')
print(person01.name)
print(person01.years_old)
person01.drinking('Coke')
person01.drinking('beer')