from samplebase import SampleBase
from rgbmatrix import graphics
import time
from bird_alert.bird_api.bird_client import BirdClient
from bird_alert.constants import API_KEY

class Alerts():
    def __init__(self, matrix):
        self.matrix = matrix

    @staticmethod
    def __parse_text():
        client = BirdClient(API_KEY)
        return client.fetch_nearby_rare()

    def set_alerts(self):
        font = graphics.Font()
        font.LoadFont("../../../fonts/7x13.bdf")
        textColor = graphics.Color(89, 158, 92)
        pos = self.matrix.width
        alert_message = self.__parse_text()

        while True:
            self.matrix.Clear()
            graphics.DrawText(offscreen_canvas, font, 35, 5, graphics.Color(255, 255, 255), "ONE")
            
            graphics.DrawText(offscreen_canvas, font, 35, 10, graphics.Color(255, 255, 255), "NICE BIRD")

            graphics.DrawText(offscreen_canvas, font, 35, 20, graphics.Color(255, 255, 255), "SPOTTED")

            graphics.DrawText(offscreen_canvas, font, 35, 30, graphics.Color(255, 255, 255), "JARDIN BOTANIQUE")

            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
