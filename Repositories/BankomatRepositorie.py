from Repositories.ConnectionMySQL import *


class BankomatRepositorieFunctions:

    def UpdateMoneyAmount( BillName, BillAmount):
        arguments = (BillAmount,BillName)
        if BillAmount > 0:
            BankomatRepositorieFunctions.MakeNoteToActions ("Инкасация")
        MyCursor.execute("Update Money Set AmountOfBill = AmountOfBill + %s Where NameOfBill = %s",arguments)
        MySQLConnection.commit()

    def GetAvailableBill():  # Return list of NameOfBill and AmountOfBill
        MyCursor.execute("Select NameOfBill, AmountOfBill From Money Where AmountOfBill > 0" )
        result = MyCursor.fetchall()
        AvailableBill = list()
        AmountOfBill = list()
        for item in result:
            AvailableBill.append(item[0])
            AmountOfBill.append(item[1])

        return AvailableBill,AmountOfBill

    def MakeNoteToActions (message : str):
        arg = (message,)
        MyCursor.execute("Insert into Actions(info, time) values(%s,NOW())", arg);
        MySQLConnection.commit()


