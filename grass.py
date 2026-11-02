from pico2d import load_image


class Grass:
    def __init__(self,y,layer):
        self.image = load_image('grass.png')
        self.y=y
        self.layer=layer

    def draw(self):
        self.image.draw(400, self.y)

    def update(self):
        pass
