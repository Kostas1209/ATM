from Models.User import User
from Models.Session import Session
import Exceptions.CustomExceptions as Excp
from Services.UserService import UserServiceFunctions
from Services.FinancialService import FinancialServiceFunctions
from Repositories.UserRepositorie import UserRepositorieFunctions 
from Repositories.BankomatRepositorie import BankomatRepositorieFunctions



def main():
    #FinancialServiceFunctions.BillAdding({ 1: 10, 2 : 10, 5 : 10, 10 : 10, 20 : 20, 50 : 10, 100 : 10, 200 : 10, 500 : 100})
    #UserServiceFunctions.AddAccount(User("Urii","Kovalenko",8445,1245,7,0))
    CurrentSession = None
    while True:
        try:
            if CurrentSession != None: #If Session is created
                raise Excp.SessionIsOver
            print("Enter user account number")
            EnterUserAccount = int(input())
            CurrentUser = UserRepositorieFunctions.GetUserInfo(EnterUserAccount)

        except Excp.AccountIsBlocked as e:
            print(e)
            continue
        except Excp.NotFoundAccount as e:
            print(e)
            continue
        except Excp.SessionIsOver:
            pass
        except ValueError:
            print("Data was entered wrong ")
            continue

        while True:
            try:
                print("Enter the password")
                EnterPassword = int(input())
                CurrentSession = Session(CurrentUser, EnterPassword)
                UserServiceFunctions.Login(CurrentSession, MenuService)
                CurrentSession = None
                break

            except Excp.BlockAccount as e:
                UserRepositorieFunctions.BlockAccount(CurrentUser.NumberOfAccount)
                BankomatRepositorieFunctions.MakeNoteToActions("Account {} is blocked for 1 minute ".format(CurrentUser.NumberOfAccount))
                CurrentSession = None
                print(e)
                break
            except Excp.WrongPassword as e:
                print(e)
                continue
            except ValueError:
                print("Wrong Argument")
                CurrentSession = None
                break
    return 

def MenuService(CurrentUser : User):

    while True:
         print("\nChange operation :")
         print("Withdraw money - 1")
         print("See balance - 2")
         print("Exit - 3")
         event = int( input() )
         if event == 1:
             try:
                 print("Available bill")
                 for item in BankomatRepositorieFunctions.GetAvailableBill() [0] :
                     print(item ,end = ' ')
                 print()
                 print("Enter password")
                 EnterPassword = int(input())
                 CurrentSession = Session(CurrentUser, EnterPassword)
                 UserServiceFunctions.Login(CurrentSession, FinancialServiceFunctions.WithdrawMoney)
                 print("Take your Money")

             except Excp.BlockAccount as e:
                 raise e
             except Excp.NotEnoughtMoney as e:
                 print(e)
             except  Excp.NotHaveBill as e:
                 print(e)

             except  Excp.BigSum as e:
                 print(e)
             except ValueError :
                 print("Wrong argument")
             break

         elif event == 2:
             try:
                print("Enter password")
                EnterPassword = int(input())
                CurrentSession = Session(CurrentUser, EnterPassword)
                UserServiceFunctions.Login(CurrentSession, UserServiceFunctions.ShowUserBalance)
             except Excp.BlockAccount as e:
                raise e
             except ValueError :
                raise ValueError
             break
                    

         elif event == 3:
             print("Good luck")
             break

         else:
             print("incorreect operation")
             break



main()
