class Stirrer:
    mixingSpeed = 0
    activated = False

    def __init__(self, speed):
        self.mixingSpeed = speed

    def set_activated(self, value):
        if value is self.activated:
            if value is True:
                print("Stirrer was already activated")
            else:
                print("Stirrer was already deactivated")
            return
        if value:
            print("Starting stirrer")
        else:
            print("Stopping stirrer")
        self.activated = value
