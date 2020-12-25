from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics
from PIL import Image, ImageDraw, ImageFont


class Marquee():
    def __init__(self):
        pass

    def set_up_marquee(self):
        font = graphics.Font()
        font.LoadFont("../more_fonts/04b_24.bdf")
        textColor = graphics.Color(89, 158, 92)

        font_ttf = ImageFont.truetype("../more_fonts/retro_computer.ttf", 7)

        image = Image.new('RGB', (30, 30))
        draw = ImageDraw.Draw(image)
        draw.rectangle([0, 6, 26, -1], fill=(255, 255, 255))
        draw.text((0, -2), "BIRD", fill=(232, 1, 3), font=font_ttf)
        self.matrix.SetImage(image)
        graphics.DrawText(self.matrix, font, 10, 10, textColor, "alert")
        self.matrix.SwapOnVSync(self.matrix)
