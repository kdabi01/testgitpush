
class Employee:
    emp_count = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@valmet.com"
        Employee.emp_count += 1

    def fname(self):
        #return self.first + " " + self.last
        return f"{self.first} {self.last}"
        #return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.emp_count)
e1 = Employee("kamlesh", "last", 50000)
e2 = Employee("jitesh", "last", 60000)
print(Employee.emp_count)