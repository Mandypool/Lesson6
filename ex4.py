# Реализуйте базовый класс Car.
# - у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# - опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# - добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# - для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} поехала!"

    def stop(self):
        return f"Машина {self.name} остановилась!"

    def turn(self, direction):
        return f"Машина {self.name} повернула " + direction

    def show_speed(self):
        return f'Скорость {self.name} составляет {self.speed}'

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейская машина'
        else:
            return f'{self.name} не является полицейским автомобилем'


class TownCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        print(f'Скорость городского автомобиля {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше скоростного режима'
        else:
            return f'Скорость {self.name} соответсвует скоростному режиму'


class SportCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)


class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        print(f'Скорость рабочей машины {self.name} составялет {self.speed}')

        if self.speed > 40:
            return f'Скорость {self.name} выше скоростного режима'
        else:
            return f'Скорость {self.name} соответсвует скоростному режиму'


class PoliceCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это полицейская машина'
        else:
            return f'{self.name} не является полицейским автомобилем'


bmw = SportCar('BMW', 110, 'черная', False)
kia = TownCar('KIA', 70, 'белая', False)
vaz = WorkCar('ВАЗ 2106', 30, 'вишневая', False)
lada = PoliceCar('Лада калина', 70, 'белая', True)
print(bmw.go())
print(bmw.show_speed())
print(bmw.turn('направо'))
print(bmw.stop())
print(kia.show_speed())
print(vaz.show_speed())
print(vaz.police())
print(lada.police())
print(kia.turn('налево'))

