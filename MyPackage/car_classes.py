
class Engine():
    def __init__(self, size, fuel, supercharged):
        self.size = size
        self.fuel = fuel
        self.supercharged = supercharged

    def sound(self):
        print('BROOOOOOOMMMM!!!!')


class General():
    type = 'automobile'

    def __init__(self, producer, model, year, color):
        self.producer = producer
        self.model = model
        self.year = year
        self.color = color
        self.name = producer + ' ' + model

    def __str__(self):
        return f'Car informations:\n\tName: {self.name},\n\tYear: {self.year}\n\tColor: {self.color}'

    def age(self):
        print(2022 - self.year)


class Car(General, Engine):
    def __init__(self, producer, model, year, color, size, fuel, supercharged):
        General.__init__(self, producer, model, year, color)
        Engine.__init__(self, size, fuel, supercharged)


def this_module():
    print('alpha')


if __name__ == '__main__':
    this_module()

if __name__ == 'MyPackage.car_classes':
    pass
