from PIL import Image


class BirdImage:
    def __init__(self, image_file, bird_width, bird_height, loc_width, loc_height):
        self.image_file = image_file
        self.bird_height = bird_height
        self.bird_width = bird_width

        self.loc_width = loc_width
        self.loc_height = loc_height

    def set_image(self, matrix):
        bird_image = Image.open(self.image_file)
        bird_image.thumbnail(
            (matrix.width - self.bird_width, matrix.height - self.bird_width),
            Image.ANTIALIAS,
        )

        matrix.SetImage(bird_image.convert("RGB"), self.loc_width, self.loc_height)
