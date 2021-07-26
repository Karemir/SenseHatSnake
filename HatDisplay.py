from HatLed import HatLed


class HatDisplay:
    def __init__(self, sense):
        self.sense = sense
        self.pixels = []

        for x in range(0, 8):
            self.pixels.append([])
            for y in range(0, 8):
                self.pixels[x].append(HatLed(x, y))

    def draw_pixels(self):
        pxs = []
        for y in range(0, 8):
            for x in range(0, 8):
                pxs.append(self.pixels[x][y].get())

        self.sense.set_pixels(pxs)

    def set_pixel(self, r, g, b, x, y):
        self.pixels[x][y].set(r, g, b)

    def get_pixel(self, x, y):
        return self.pixels[x][y]

    def clear(self):
        self.sense.clear()
        for px in self.pixels:
            for py in px:
                py.set(0, 0, 0)
