from Repositories.BankomatRepositorie import BankomatRepositorieFunctions
from Repositories.UserRepositorie import UserRepositorieFunctions
from Models.User import User
from Models.Session import Session
from Decorators.Decorators import CheckSessionDecorator


class UserServiceFunctions: 

    def ShowUserBalance(CurrentUser : User):
        BankomatRepositorieFunctions.MakeNoteToActions("Checking balance in account {}".format(CurrentUser.NumberOfAccount))
        print(CurrentUser.AmountOfMoney)
        return 

    def AddAccount(CurrentUser : User):
        if UserRepositorieFunctions.IsUserExists(CurrentUser.Name, CurrentUser.Surname) == False:
            UserRepositorieFunctions.AddNewUser(CurrentUser.Name, CurrentUser.Surname)
        UserRepositorieFunctions.AddNewAccount(CurrentUser)
        return 

    @CheckSessionDecorator
    def Login(session : Session, function):
        function(session.SessionUser)
        return 
