
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@valmet.com"

    def fname(self):
        #return self.first + " " + self.last
        return f"{self.first} {self.last}"
        #return "{} {}".format(self.first, self.last)


e1 = Employee("kamlesh", "last", 50000)
e2 = Employee("jitesh", "last", 60000)

#print(e1, e2)

#e1.first = "Kamlesh"
#e1.last = "dabi"
#e1.email = "kalesh.dabi@valmet.com"
#e1.pay = 50000

#e2.first = "Jitesh"
#e2.last = "Sahu"
#e2.email = "jitesh.sahu@valmet.com"
#e2.pay = 62000

print(e1.email)
print(e2.email)
print(e1.fname())



