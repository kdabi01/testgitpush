import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
#logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('New Employee: {} - {}'.format(self.fullname, self.email))
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

e1 = Employee('kamlesh', 'dabi')
e2 = Employee('Jitesh', 'sahu')
e3 = Employee('harish', 'sharma')
