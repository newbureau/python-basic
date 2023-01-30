"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    """ Exception LowFuelError"""
    pass


class NotEnoughFuel(Exception):
    """ Exception NotEnoughFuel"""
    pass


class CargoOverload(Exception):
    """ Exception CargoOverload"""
    pass
