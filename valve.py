class Valve:
    volumePS = 0
    open = False

    def __init__(self, volume, direction):
        self.volumePS = volume
        self.direction = direction

    def set_open(self, value):
        if value is self.open:
            if value is True:
                print("Valve was already opened")
            else:
                print("Valve was already closed")
        self.open = value
