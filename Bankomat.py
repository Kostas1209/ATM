from Models.User import User
from Models.Money import Money
import Exceptions.CustomExceptions as Excp
from Services.UserService import UserServiceFunctions
from Services.FinancialService import FinancialServiceFunctions
from Repositories.UserRepositorie import UserRepositorieFunctions 
from Repositories.BankomatRepositorie import BankomatRepositorieFunctions

from Decorators.Decorators import CheckPasswordDecorator


def main():
    #FinancialServiceFunctions.BillAdding({ 1: 10, 2 : 10, 5 : 10, 10 : 10, 20 : 20, 50 : 10, 100 : 10, 200 : 10, 500 : 10})
    #UserServiceFunctions.AddAccount(User("Urii","Kovalenko",8445,1245,7,0))
    while True:
        print("Enter user account number")
        try:
            EnterUserAccount = int(input())
            CurrentUser = UserRepositorieFunctions.GetUserInfo(EnterUserAccount)

        except Excp.AccountIsBlocked as e:
            print(e)
        except Excp.NotFoundAccount as e:
            print(e)
        except ValueError:
            print("Data was entered wrong ")

        else:
            try:
                MenuService(CurrentUser)

            except ValueError:
                print("Wrong Argument")

            except Excp.BlockAccount as e:
                print(e)


    return 

@CheckPasswordDecorator
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
                 FinancialServiceFunctions.WithdrawMoney(CurrentUser)

             except Excp.BlockAccount as e:
                 raise e
             except Excp.NotEnoughtMoney as e:
                 print(e)
                 continue
             except  Excp.NotHaveBill as e:
                 print(e)
                 continue
             except  Excp.BigSum as e:
                 print(e)
                 continue
             except ValueError :
                 print("Wrong argument")
                 continue

         elif event == 2:
             try:
                UserServiceFunctions.ShowUserBalance(CurrentUser)
             except Excp.BlockAccount as e:
                raise e
             except Exception as e:
                print(e)
                    

         elif event == 3:
             print("Всего хорошего")
             break

         else:
             print("Error")



main()
