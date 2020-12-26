#!/usr/bin/env python
import time
import sys
from samplebase import SampleBase
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from rgbmatrix import graphics
from PIL import Image, ImageDraw, ImageFont

from bird_alert.layout.bird_image import BirdImage
from bird_alert.layout.marquee import Marquee
from constants import BirdContants
from bird_alert.layout.alerts import Alerts
from bird_alert.bird_api.bird_client import BirdClient


class BirdMonitor(SampleBase):
    def __init__(self, *args, **kwargs):
        super(BirdMonitor, self).__init__(*args, **kwargs)
        self.parser.add_argument(
            "-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()

        bird_image = BirdImage(BirdContants.BIRD_PIC.value)
        marquee = Marquee(BirdContants.SIG_FONT.value, BirdContants.MARQUEE_FONT.value)
        alerts = Alerts(BirdContants.SMALL_FONT.value)
        client = BirdClient(BirdContants.API_KEY.value)

        spotted_bird = client.fetch_nearby_rare()

        pos = offscreen_canvas.width


        
        while True:
            offscreen_canvas.Clear()

            marquee.set_up_marquee(offscreen_canvas)
            

            pos, total_length = alerts.set_alerts(offscreen_canvas, pos, spotted_bird)

            bird_image.set_image(offscreen_canvas)

            if (pos + total_length < 0):
                pos = offscreen_canvas.width

            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

            # Main function
if __name__ == "__main__":
    run_text = BirdMonitor()
    if (not run_text.process()):
        run_text.print_help()
