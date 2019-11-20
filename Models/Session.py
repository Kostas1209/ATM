from Models.User import User 

class Session(object):
    
    def __init__(self,CurrentUser : User, EnterPin : int):
        self.__SessionUser = CurrentUser
        self.__EnterPin = EnterPin

    @property
    def SessionUser (self):
        return self.__SessionUser

    @property
    def EnterPin(self):
        return self.__EnterPin

    @EnterPin.setter
    def EnterPin(self,value):
        try:
            value = int(value)
            self.__EnterPin = value
        except:
            self.__EnterPin = -1

