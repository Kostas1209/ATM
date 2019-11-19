from Repositories.BankomatRepositorie import BankomatRepositorieFunctions
from Repositories.UserRepositorie import UserRepositorieFunctions
from Models.User import User
from Decorators.Decorators import CheckPasswordDecorator
import Exceptions.CustomExceptions as Excp

class FinancialServiceFunctions:
    
    
    def TakeMoneyFromBankomat(WithdrawSum):
        AvailableBill , AmountOfBill = BankomatRepositorieFunctions.GetAvailableBill()
        result = dict()
        AmountOfBillGivenUser = 0
        for i in range( len(AvailableBill)-1, -1 , -1):
            if WithdrawSum // AvailableBill[i] * AvailableBill[i] <= AmountOfBill[i] * AvailableBill[i] and WithdrawSum // AvailableBill[i]>0:
                result[ AvailableBill[i] ] = WithdrawSum // AvailableBill[i]
                AmountOfBillGivenUser += (WithdrawSum // AvailableBill[i] )
                WithdrawSum -= WithdrawSum // AvailableBill[i] * AvailableBill[i]
            elif WithdrawSum // AvailableBill[i] > 0:
                result[ AvailableBill[i] ] = AmountOfBill[i] 
                AmountOfBillGivenUser += AmountOfBill[i] 
                WithdrawSum -= AmountOfBill[i] * AvailableBill[i]
        if AmountOfBillGivenUser > 20:
            raise Excp.BigSum("sum is so big more than 20 bills")
        if WithdrawSum > 0:
            raise Excp.NotHaveBill("We can`t give you this sum")
        print(result)
        for Key ,value in result.items():
            BankomatRepositorieFunctions.UpdateMoneyAmount(Key, -1*value)
        print("Заберите ваши деньги")

        return 

    @CheckPasswordDecorator
    def WithdrawMoney(CurrentUser : User ):
        print("How many you want to withdraw?")
        WithdrawSum = int( input() )

        if WithdrawSum > CurrentUser.AmountOfMoney:
            BankomatRepositorieFunctions.MakeNoteToActions("Попытка снятия денег на счёте {}".format(CurrentUser.NumberOfAccount))
            raise Excp.NotEnoughtMoney("Not Enough money in the account")
        
        FinancialServiceFunctions.TakeMoneyFromBankomat(WithdrawSum)
        UserRepositorieFunctions.UpdateUserMoney(-1 * WithdrawSum, CurrentUser)
        BankomatRepositorieFunctions.MakeNoteToActions("На аккаунте {} снято {}".format(CurrentUser.NumberOfAccount,WithdrawSum))

        return 

    def BillAdding(RecevedBill : dict):

        for Key, value in RecevedBill.items():
            BankomatRepositorieFunctions.UpdateMoneyAmount(Key,value)
        return