class car :
    def __init__(self, body, engin, tyre):
        self.body = body
        self.engin = engin
        self.tyre = tyre

    def milage (self):
        print("milage of this car ")

class Tata(car):
    pass

car1 = car("solid", "v6", "radial")

#print(car1.milage())

t = Tata("solid", "v6", "radial")

print(t.milage())