class Alarm: # use noun
    def __init__(self, state: bool) -> None:
        self.__state = state # use noun

    def get_state(self, ) -> bool: # verb
        return self.__state
    
    def set_state(self, value: bool) -> None:
        self.__state = value

   
al = Alarm(False)
print(al.get_state())
al.set_state(True)
print(al.get_state())



