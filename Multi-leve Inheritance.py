# Multi level Inheritance

class bank :
    def transations(self):
        print("total trnasation value")

    def account_opening(self):
        print("this will show you your account ioen status")

    def deposit(self):
        print("this will show deposited amount")

class HDFCBank(bank):
    def hdfc_to_icici(self):
        print("this will show you all the transations happened to icici through hdfc.")

class ICICIBank(HDFCBank):
    pass

i = ICICIBank()

i.transations()
i.deposit()
i.account_opening()
i.hdfc_to_icici()

