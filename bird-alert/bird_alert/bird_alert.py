#!/usr/bin/env python
import time
import sys
from samplebase import SampleBase
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics
from PIL import Image, ImageDraw, ImageFont

from layout.bird_image import BirdImage
from layout.marquee import Marquee
from constants import BirdContants
from layout.alerts import Alerts

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument(
            "-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()

        bird_image = BirdImage(BirdContants.BIRD_PIC.value)
        marquee = Marquee(BirdContants.SMALL_FONT.value, BirdContants.MARQUEE_FONT.value)
        alerts = Alerts(irdContants.SMALL_FONT.value)


        font = graphics.Font()

        font.LoadFont(BirdContants.SMALL_FONT.value)
        pos = offscreen_canvas.width

        scrolling = self.matrix.CreateFrameCanvas()
        while True:
            offscreen_canvas.Clear()

            marquee.set_up_marquee(offscreen_canvas)
            
            # graphics.DrawText(offscreen_canvas, font, 35, 5, graphics.Color(255, 255, 255), "ONE")
            
            # graphics.DrawText(offscreen_canvas, font, 35, 10, graphics.Color(255, 255, 255), "NICE BIRD")

            alerts.set_alerts(offscreen_canvas, pos)
            # len = graphics.DrawText(offscreen_canvas, font, pos, 20, graphics.Color(255, 255, 255), "LAURENT BASTIEN CORBEIL")

            bird_image.set_image(offscreen_canvas)

            pos -= 1

            if (pos < 0):
                pos = offscreen_canvas.width

            time.sleep(0.1)
            scrolling = self.matrix.SwapOnVSync(scrolling)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            # Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
