#Dtata abstraction - hide a data behind someone
class ineuron:
    __students = "data science"


    def students(self):
        print("print the class of students", ineuron.__students)

s = ineuron()

s.students()
print(s._ineuron__students)

