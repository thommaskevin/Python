class MyClass:
    '''
    Constructor methods
    '''
    def __init__(self, attributes):
        self.my_attributes = attributes
        self.my_attributes2 = 'Hellow Word'
    
    '''
    Other methods
    '''
    def my_method(self):
        print(self.my_attributes)
        print(self.my_attributes2)
    
    def my_method_mult(self, num, mult):
        return num * mult


object = MyClass(23)
object.my_method()