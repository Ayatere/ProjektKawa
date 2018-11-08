class Pump:
    volumePS = 0
    activated = False

    def __init__(self, volume, direction):
        self.volumePS = volume
        self.direction = direction

    def set_activated(self, value):
        if value is self.activated:
            if value is True:
                print("Pump was already activated")
            else:
                print("Pump was already deactivated")
            return
        self.activated = value

    def action(self, tanks):
        if tanks[0].level > self.volumePS:
            if tanks[1].level + self.volumePS < tanks[1].capacity:
                tanks[0].level -= self.volumePS
                tanks[1].level += self.volumePS
            else:
                print("Tank is too full to pump more fluid into")
        else:
            print("Pump can't work with that amount of fluid")
