from abc import ABC


# import exceptions
from homework_02 import exceptions


class Vehicle(ABC):
    def __init__(self, weight: int = 500,
                 fuel: int = 50,
                 fuel_consumption: int = 10,
                 started: bool = False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError("Low fuel")

    def move(self, distance):
        if self.fuel >= self.fuel_consumption * distance:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise exceptions.NotEnoughFuel("Not enough fuel")
