from PIL import Image


class BirdImage:
    def __init__(self, image_file):
        self.image_file = image_file

    def set_image(self, matrix):
        bird_image = Image.open(self.image_file)
        bird_image.thumbnail((matrix.width - 5, matrix.height - 5), Image.ANTIALIAS)

        matrix.SetImage(bird_image.convert("RGB"), 0, 15)
