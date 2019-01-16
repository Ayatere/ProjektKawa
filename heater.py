class Heater:
    heatingPower = 100
    activated = False

    def __init__(self, heating_power):
        self.heatingPower = heating_power

    def set_activated(self, value):
        if value is self.activated:
            if value is True:
                print("Heater was already activated")
            else:
                print("Heater was already deactivated")
            return
        if value:
            print("Starting heater")
        else:
            print("Stopping heater")
        self.activated = value
