class Pixel:
    def __init__(self, x, y):
        self.r = 0
        self.g = 0
        self.b = 0
        self.x = x
        self.y = y
        self.fadeAmount = 40

    def get(self):
        # return a bit darker colors, diodes are too bright for 255.
        return [self.r / 2, self.g / 2, self.b / 2]

    def set(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def fade(self):
        self.r -= self.fadeAmount
        self.g -= self.fadeAmount
        self.b -= self.fadeAmount
        if self.r < 0:
            self.r = 0
        if self.g < 0:
            self.g = 0
        if self.b < 0:
            self.b = 0
