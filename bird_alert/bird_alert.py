#!/usr/bin/env python
import time
import sys
from samplebase import SampleBase
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics
from PIL import Image, ImageDraw, ImageFont


class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument(
            "-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        bird_file = "cardinal.png"
        bird_image = Image.open(bird_file)
        bird_image.thumbnail(
            (self.matrix.width-5, self.matrix.height-5), Image.ANTIALIAS)
        font = graphics.Font()
        font.LoadFont("../../../fonts/4x6.bdf")
        font.LoadFont("../more_fonts/04b_24.bdf")
        textColor = graphics.Color(89, 158, 92)
        offscreen_canvas = self.matrix.CreateFrameCanvas()

        font_ttf = ImageFont.truetype("../more_fonts/retro_computer.ttf", 7)

        while True:
            image = Image.new('RGB', (30, 30))
            draw = ImageDraw.Draw(image)
            draw.rectangle([0, 6, 26, -1], fill=(255, 255, 255))
            draw.text((0, -2), "BIRD", fill=(232, 1, 3), font=font_ttf)
            offscreen_canvas.SetImage(image)
            graphics.DrawText(offscreen_canvas, font, 10, 10, textColor, "alert")
            graphics.DrawText(offscreen_canvas, font, 35, 20, graphics.Color(255, 255, 255), "lol")
            offscreen_canvas.SetImage(bird_image.convert('RGB'), 0, 15)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            # Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
