from Repositories.BankomatRepositorie import BankomatRepositorieFunctions
from Repositories.UserRepositorie import UserRepositorieFunctions
from Models.User import User
from Decorators.Decorators import CheckPasswordDecorator


class UserServiceFunctions: 

    @CheckPasswordDecorator
    def ShowUserBalance(CurrentUser : User):
        BankomatRepositorieFunctions.MakeNoteToActions("Просмотр счета на аккаунте {}".format(CurrentUser.NumberOfAccount))
        print(CurrentUser.AmountOfMoney)
        return 

    def AddAccount(CurrentUser : User):
        if UserRepositorieFunctions.IsUserExists(CurrentUser.Name, CurrentUser.Surname) == False:
            UserRepositorieFunctions.AddNewUser(CurrentUser.Name, CurrentUser.Surname)
        UserRepositorieFunctions.AddNewAccount(CurrentUser)
        return 





        
