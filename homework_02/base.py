from abc import ABC


# import exceptions
from homework_02 import exceptions


class Vehicle(ABC):
    def __init__(self, weight: int = 50, started: bool = False, fuel: int = 10, fuel_consumption: int = 1):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        if self.fuel >= self.fuel_consumption * distance:
            self.fuel = self.fuel - self.fuel_consumption * distance
        else:
            raise exceptions.NotEnoughFuel

