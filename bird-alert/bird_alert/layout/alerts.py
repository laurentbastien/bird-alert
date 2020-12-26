from rgbmatrix import graphics
import time
from bird_alert.bird_api.bird_client import BirdClient
from bird_alert.constants import BirdContants

class Alerts():
    def __init__(self, alert_font):
        self.alert_font = alert_font

    @staticmethod
    def __parse_text():
        client = BirdClient(BirdContants.API_KEY.value)
        return client.fetch_nearby_rare()

    def set_alerts(self, matrix, pos):
        font = graphics.Font()
        font.LoadFont(self.alert_font)
        textColor = graphics.Color(89, 158, 92)
        alert_message = self.__parse_text()

        graphics.DrawText(matrix, font, pos, 10, textColor, "my_text")

        pos -= 1
        if (pos < 0):
            pos = offscreen_canvas.width

        time.sleep(0.05)
        
        matrix.SwapOnVSync(matrix)

        return pos

