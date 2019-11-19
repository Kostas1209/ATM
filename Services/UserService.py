from Repositories.BankomatRepositorie import BankomatRepositorieFunctions
from Repositories.UserRepositorie import UserRepositorieFunctions
from Services.FinancialService import FinancialServiceFunctions
from Models.User import User
from Models.Money import Money
from Decorators.Decorators import CheckPasswordDecorator
import Exceptions.CustomExceptions as Excp


class UserServiceFunctions: 

    @CheckPasswordDecorator
    def MenuService(CurrentUser : User):

        while True:
            print("\nВыберите операцию :")
            print("Снять деньги со счёта - 1")
            print("Посмотреть баланс счёта - 2")
            print("Закончить операцию - 3")
            event = int( input() )
            if event == 1:
                try:
                    print("Доступные купюры")
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





        
