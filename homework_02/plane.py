"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, cargo=0, max_cargo=2000):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, number):
        if self.cargo + number <= self.max_cargo:
            self.cargo += number
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        cargo_old = self.cargo
        self.cargo = 0
        return cargo_old
