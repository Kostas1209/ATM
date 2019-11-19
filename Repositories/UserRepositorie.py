from Repositories.ConnectionMySQL import *
from Models.User import User
import Exceptions.CustomExceptions as Excep


class UserRepositorieFunctions:
    def UpdateUserMoney(WithdrawSum : int, CurrentUser : User):
        arguments = (WithdrawSum, CurrentUser.NumberOfAccount)
        MyCursor.execute("Update accounts Set Money = Money + %s Where AccountNumber = %s",arguments)
        MySQLConnection.commit()

    def RefreshUserBlocked(accountNumber):
        arg = (accountNumber,)
        MyCursor.execute("""Update accounts 
                            Set BlockedTime = Null 
                            Where AccountNumber = %s and BlockedTime Is Not Null and Date_add(BlockedTime,interval 1 Minute) < NOW()
        """,arg)
        MySQLConnection.commit()

    def GetUserInfo(NumberOfAccount : int ) -> User:

        UserRepositorieFunctions.RefreshUserBlocked(NumberOfAccount) ## Check user is blocked
        if UserRepositorieFunctions.IsAccountBlocked(NumberOfAccount) == True:
            raise Excep.AccountIsBlocked("Account is blocked")
        NumberOfAccount = (NumberOfAccount,)
        MyCursor.execute("SELECT AccountNumber,CardNumber, Pin, Money FROM accounts WHERE accountnumber = %s ",NumberOfAccount)
        accountInfo = MyCursor.fetchone() ## Account information 
        MyCursor.execute("""SELECT Name , SurName From users 
                            Where id IN ( Select Id From accounts Where AccountNumber = %s);""" ,NumberOfAccount)
        if accountInfo == None:
            raise Excep.NotFoundAccount("Данный номер счёта не найден")
        NameInformation = MyCursor.fetchone() ## Name and Surname 
        CurrentUser = User(NameInformation[0],NameInformation[1],accountInfo[0],accountInfo[1],\
                           accountInfo[2],accountInfo[3])

        return CurrentUser

    def IsAccountBlocked(NumberOfAccount : int):
        arguments = (NumberOfAccount,)
        MyCursor.execute("Select BlockedTime from accounts where AccountNumber = %s and BlockedTime is Not Null",arguments)
        result = MyCursor.fetchone()
        return result != None

    def IsUserExists(Name : str , Surname : str):
        arg = (Name ,Surname)
        MyCursor.execute("Select id from users where Name = %s and Surname = %s",arg)
        result = MyCursor.fetchone()
        return result != None

    def AddNewUser(Name, Surname):
        arg = (Name, Surname)
        MyCursor.execute("""Insert users (Name,Surname) values (%s,%s)""",arg)
        MySQLConnection.commit()
      
    def AddNewAccount(CurrentUser : User):
        arg = (CurrentUser.Name, CurrentUser.Surname, CurrentUser.NumberOfAccount, CurrentUser.NumberOfCard, CurrentUser.Pin, CurrentUser.AmountOfMoney)
        MyCursor.execute("""Insert accounts (id,AccountNumber, CardNumber, Pin, Money)
                            values ((Select id from users where Name = %s and Surname = %s) ,%s,%s,%s,%s) """,arg)
        MySQLConnection.commit()

    def BlockAccount(NumberOfAccount : int):
        arguments = (NumberOfAccount,)
        MyCursor.execute("Update accounts Set blockedTime = NOW() where AccountNumber = %s",arguments)
        MySQLConnection.commit()
        return 




