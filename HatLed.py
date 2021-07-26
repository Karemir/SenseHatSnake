class HatLed:
    def __init__(self, x, y):
        self.r = 0
        self.g = 0
        self.b = 0
        self.x = x
        self.y = y
        self.fadeAmount = 40

    def get(self):
        # return a bit darker colors, LEDs are too bright for 255.
        return [self.r / 3, self.g / 3, self.b / 2]

    def set(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
