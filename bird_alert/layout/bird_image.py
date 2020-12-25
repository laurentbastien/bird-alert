from PIL import Image


class BirdImage():
    def __init__(self, matrix, image_file):
        self.matrix = matrix
        self.image_file = image_file

    def set_image(self):
        bird_image = Image.open(self.image_file)
        bird_image.thumbnail(
            (self.matrix.width-5, self.matrix.height-5), Image.ANTIALIAS)

        self.matrix.SetImage(bird_image.convert('RGB'), 0, 15)
        self.matrix.SwapOnVSync(self.matrix)
