class Car:
    pass
class Battery:
    def __init__(self):
        self.__battery_level = 80
    def read_battery_meter(self):
        print(f"Battery level: {self.__battery_level}%")
class ElectricCar(Car):
    def __init__(self, maker, model, year):
        super().__init__()
        self.maker = maker
        self.model = model
        self.year = year
        self.battery = Battery()

my_E_car = ElectricCar('tesla', 'model S', '2022')
my_E_car.battery.read_battery_meter()