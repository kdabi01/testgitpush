class Employee:
    emp_count = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@valmet.com"
        Employee.emp_count += 1

    def fullname(self):
        #return self.first + " " + self.last
        return f"{self.first} {self.last}"
        #return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    pass

dev1 = Developer('kamlesh', 'dabi', 5000)
dev2 = Developer('jitesh', 'sahu', 6000)

#print(help(Developer))

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)