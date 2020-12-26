from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics
from PIL import Image, ImageDraw, ImageFont


class Marquee():
    def __init__(self, sig_font_type, marquee_font):
        self.sig_font_type = sig_font_type
        self.marquee_font = marquee_font

    def __set_up_logo(self, matrix):
        font_ttf = ImageFont.truetype(self.marquee_font, 7)

        image = Image.new('RGB', (30, 30))
        draw = ImageDraw.Draw(image)
        draw.rectangle([0, 6, 26, -1], fill=(255, 255, 255))
        draw.text((0, -2), "BIRD", fill=(232, 1, 3), font=font_ttf)
        matrix.SetImage(image)

    def __set_up_signature(self, matrix):
        font = graphics.Font()
        font.LoadFont(self.sig_font_type)
        textColor = graphics.Color(89, 158, 92)
        graphics.DrawText(matrix, font, 10, 10, textColor, "alert")


    def set_up_marquee(self, matrix):
        self.__set_up_logo(matrix)
        self.__set_up_signature(matrix)
