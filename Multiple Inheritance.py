# Multiple Inheritance

class bank :
    def transations(self):
        print("total trnasation value")

    def account_opening(self):
        print("this will show you your account ioen status")

    def deposit(self):
        print("this will show deposited amount")

    def test(self):
        print("this is test method from bank class")

class HDFCBank():
    def hdfc_to_icici(self):
        print("this will show you all the transations happened to icici through hdfc.")

    def test(self):
        print("this is test method from HDFCBank class")

class ineuron_bank:
    def account_Status_icici(self):
        print("print a account status in icici.")

class ICICIBank (HDFCBank, bank, ineuron_bank):
    pass

i = ICICIBank()

i.transations()
i.account_opening()
i.deposit()
i.hdfc_to_icici()
i.test()
i.account_Status_icici()

