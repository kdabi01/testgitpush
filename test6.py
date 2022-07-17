class ineuron:
    def students(self):
        print("print by ineuron")

class class_type:
    def students(self):
        print("print by class type")

def ineuron_external(a):
    a.students()

i = ineuron()
j = class_type()

ineuron_external(i)
ineuron_external(j)