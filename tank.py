from stirrer import Stirrer
from heater import Heater
from valve import Valve


class Tank:
    capacity = 0
    level = 0
    temperature = 25

    def __init__(self, capacity, stirrer, heater, valve):
        self.capacity = capacity
        if stirrer is Stirrer:
            self.stirrer = stirrer
        if heater is Heater:
            self.heater = heater
        if valve is Valve:
            self.valve = valve
