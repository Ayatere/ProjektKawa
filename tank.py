from stirrer import Stirrer
from heater import Heater
from valve import Valve


class Tank:
    capacity = 0
    level = 0
    temperature = 25

    def __init__(self, capacity, stirrer, heater, valve):
        self.capacity = capacity
        if isinstance(stirrer, Stirrer):
            self.stirrer = stirrer
        if isinstance(heater, Heater):
            self.heater = heater
        if isinstance(valve, Valve):
            self.valve = valve
