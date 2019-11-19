from Models.User import User
from Models.Money import Money
from Services.UserService import UserServiceFunctions
from Repositories.UserRepositorie import UserRepositorieFunctions 
import Exceptions.CustomExceptions as Excp


def main():
    #Services.FinancialService.BillAdding({ 1: 10, 2 : 10, 5 : 10, 10 : 10, 20 : 20, 50 : 10, 100 : 10, 200 : 10, 500 : 10})
    #Services.UserService.AddAccount(User("Urii","Kovalenko",8445,1245,7,0))
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
                UserServiceFunctions.MenuService(CurrentUser)

            except ValueError:
                print("Wrong Argument")

            except Excp.BlockAccount as e:
                print(e)


    return 



main()
