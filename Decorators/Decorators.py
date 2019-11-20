from Models.Session import Session
from Repositories.UserRepositorie import UserRepositorieFunctions
from Repositories.BankomatRepositorie import BankomatRepositorieFunctions
import Exceptions.CustomExceptions as Excp

def CheckSessionDecorator(func ): 
    def Function(CurrentSession : Session,f):
        if CurrentSession.SessionUser.Pin == CurrentSession.EnterPin:
           CurrentSession.SessionUser.AmountIncorrectPassword = 0
           UserRepositorieFunctions.UpdateUserIncorrectPassword(CurrentSession.SessionUser, 0)
           func(CurrentSession,f)
           return 

        else:
           UserRepositorieFunctions.UpdateUserIncorrectPassword(CurrentSession.SessionUser, CurrentSession.SessionUser.AmountIncorrectPassword + 1)
           CurrentSession.SessionUser.AmountIncorrectPassword += 1

        if CurrentSession.SessionUser.AmountIncorrectPassword >= 3:
           UserRepositorieFunctions.UpdateUserIncorrectPassword(CurrentSession.SessionUser, 0)
           raise Excp.BlockAccount("Account have been blocked")
        else: 
           raise Excp.WrongPassword("Password is wrong")

    return Function
