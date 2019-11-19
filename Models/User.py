

class User :

    def __init__( self , Name : str, Surname : str, NumberOfAccount : int , \
		         NumberOfCard : int , Pin : int , AmountOfMoney : int ):
        self.__Name = Name
        self.__Surname =  Surname
        self.__NumberOfCard = NumberOfCard
        self.__NumberOfAccount = NumberOfAccount
        self.__Pin = Pin
        self.__AmountOfMoney = AmountOfMoney

    def __str__(self):
       return "Пользователь {0} {1} \nТекущая сумма на счету {2}".format(self.__Name,self.__Surname,self.__AmountOfMoney) 

    @property
    def Name(self):
        return self.__Name

    @property
    def Surname(self):
        return self.__Surname

    @property
    def NumberOfCard(self):
        return self.__NumberOfCard

    @property
    def NumberOfAccount(self):
        return self.__NumberOfAccount

    @property
    def Pin(self):
        return self.__Pin
    
    @property
    def AmountOfMoney(self):
        return self.__AmountOfMoney

    @AmountOfMoney.setter
    def AmountOfMoney(self,value):
        self.__AmountOfMoney = value




