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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, new_string):
        first, last, pay = new_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


e1 = Employee("kamlesh", "last", 50000)
e2 = Employee("jitesh", "last", 60000)

#e1 = 'kamlesh-dabi-50000'
#e2 = 'jitesh-sahu-60000'
#e3 = 'hitesh-sharma-70000'

import datetime
my_date = datetime.date(2022, 7, 11)

print(Employee.is_workday(my_date))