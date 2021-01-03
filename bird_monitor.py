import random
import sys
import time

from bird_alert.bird_api.bird_client import BirdClient
from bird_alert.layout.alerts import Alerts
from bird_alert.layout.bird_image import BirdImage
from bird_alert.layout.marquee import Marquee
from bird_alert.rgb_base import RGBBase
from constants import BirdContants, BirdOne, BirdTwo


class BirdMonitor(RGBBase):
    def __init__(self, *args, **kwargs):
        super(BirdMonitor, self).__init__(*args, **kwargs)

    @staticmethod
    def get_alert_length():
        return time.time() + BirdContants.ALERT_LENGTH.value

    @staticmethod
    def bird_switch():
        birds = (BirdOne, BirdTwo)
        current_bird = random.choice(birds)

        bird_image = BirdImage(
            current_bird.BIRD_PIC.value,
            current_bird.WIDTH.value,
            current_bird.HEIGHT.value,
            current_bird.LOC_WIDTH.value,
            current_bird.LOC_HEIGHT.value,
        )

        return bird_image

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        bird_image = self.bird_switch()
        t_end = self.get_alert_length()

        marquee = Marquee(BirdContants.SIG_FONT.value, BirdContants.MARQUEE_FONT.value)
        alerts = Alerts(BirdContants.SMALL_FONT.value)
        client = BirdClient(BirdContants.API_KEY.value)

        spotted_bird = client.fetch_nearby_rare()

        pos = offscreen_canvas.width

        while time.time() < t_end:
            offscreen_canvas.Clear()

            marquee.set_up_marquee(offscreen_canvas)

            pos, total_length = alerts.set_alerts(offscreen_canvas, pos, spotted_bird)

            bird_image.set_image(offscreen_canvas)

            if pos + total_length < 0:
                pos = offscreen_canvas.width

            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


if __name__ == "__main__":
    run_text = BirdMonitor()
    if not run_text.process():
        run_text.print_help()
