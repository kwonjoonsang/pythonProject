#Class Study
class Car:
    def __init__(self, tp, color):
        self.type = tuple
        self.color = color
        self.tp = tp

    def show(self):
        return "Car Class"

class BmwCar(Car):
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self):
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self):
        return "Your Car Name : %s" % self.car_name

    def show(self):
        print(super().show())
        return "Car Info : %s %s %s" % (self.car_name, self.type, self.color)

model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)
print(model1.type)
print(model1.tp)
print(model1.car_name)
print(model1.show())
print(model1.show_model())
print(model1.__dict__)

model2 = BenzCar('220d', 'sedan', 'white')
model2.show()

model3 = BenzCar('S Class', 'sedan', 'silver')
print(model3.show())

# Inheritance Info
print(BmwCar.mro())
print(BenzCar.mro())

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())