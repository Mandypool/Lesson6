# Реализовать класс Road (дорога).
# - определить атрибуты: length (длина), width (ширина);
# - значения атрибутов должны передаваться при создании экземпляра класса;
# - атрибуты сделать защищёнными;
# - определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# - использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1
# см*число см толщины полотна;
# - проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    _length = None # длина
    _width = None # ширина
    weigth = None # масса
    thickness = None # толщина

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def intake(self):
        self.weigth = 25
        self.thickness = 0.05
        intake = self.length * self.width * self.weigth * self.thickness
        print(intake)


my_road = Road(20000, 5)
my_road.intake()
