from Models.User import User
from Repositories.UserRepositorie import UserRepositorieFunctions
from Repositories.BankomatRepositorie import BankomatRepositorieFunctions
import Exceptions.CustomExceptions as Excp

def CheckPasswordDecorator( func ): 
    def Function(CurrentUser : User):
        counter = 3
        while True:
            if counter <= 0:
                UserRepositorieFunctions.BlockAccount(CurrentUser.NumberOfAccount)
                BankomatRepositorieFunctions.MakeNoteToActions("Account {} is blocked for 1 minute ".format(CurrentUser.NumberOfAccount))
                raise Excp.BlockAccount("Account is blocked for 1 minute")
                break
            print("Enter the password")
            try:
                EnterPassword = int( input() )
            except:
                counter -= 1
                print("Password is wrong")
                continue

            if CurrentUser.Pin == EnterPassword:
                func(CurrentUser)
                break
            else:
                counter -= 1
                print("Password is wrong")


    return Function
