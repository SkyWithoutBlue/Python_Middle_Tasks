#Car.py
from CarComponent import Engine
from math import pi


class Car():
    def __init__(self, maker, model, year):
        self._maker = maker
        self._model = model
        self._year = year

    def add_components_to_car(self, **components):
        components_keys = components.keys()
        if "engine" in components_keys:
            self._engine = components["engine"]
        else:
            raise ValueError("No engines")
        self._speed = 2 * pi * 12 * self._engine.get_power()

    def get_speed(self):
        return self._speed

    def get_name(self):
        return f"{self._maker} {self._model} {self._year}"

  #CarComponent.py
class CarComponent():
    _name: str

    def get_name(self):
        return self._name


class Engine(CarComponent):
    def __init__(self, name, power):
        self._name = name
        self._power = power

    def get_power(self):
        return self._power

  #CarFabrick.py
from Car import Car
from CarComponent import Engine


class CarFabrick():
    _cars=[]
    _engine_list = [
        Engine("Форд", 1.5),
        Engine("Форд", 1.8),
        Engine("Ферари", 2)
    ]
    _engine_dict = {index: value for index, value in enumerate(_engine_list)}

    def _print_engine(self):
        for index, engine in self._engine_dict.items():
            print(index, engine.get_name(), engine.get_power())

    def _pick_engine(self):
        index_engine = input("Введите номер выбраного мотора")
        return self._engine_dict[int(index_engine)]

    def create_car(self):
        self._print_engine()
        while True:

            maker = input("Введите производителя машины")
            model = input("Введите модель машины")
            year = input("Введите год изготовления машины")
            car = Car(maker, model, year)
            car.add_components_to_car(engine=self._pick_engine())
            self._cars.append(car)
            user_chose = input("Введите выход для выхода из конструктора").strip().lower()
            if user_chose == "выход":
                break

    def get_cars(self):
        return self._cars

  #main.py
from Track import Track
from CarFabrick import CarFabrick

if __name__ == "__main__":
    car_fabric = CarFabrick()
    car_fabric.create_car()
    track = Track(int(input("Введите длину трассы")), car_fabric.get_cars())
    track.ride()

#Track.py
class Track():
    def __init__(self, length, cars):
        self._length = length
        self._cars = cars

    def ride(self):
        print("Ride")
        print("Участники: ")
        for car in self._cars:
            print(car.get_name())
        print("Вычисляю результат ... ")
        print("...")
        result_tab = sorted(self._cars, key=lambda car: self._length / car.get_speed())
        for i in range(len(result_tab)):
            print(f"{i + 1} место: {result_tab[i].get_name()}")
