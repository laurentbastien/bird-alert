from rgbmatrix import graphics
import time

class Alerts():
    def __init__(self, alert_font):
        self.alert_font = alert_font

    def set_alerts(self, matrix, pos, spotted_bird):
        font = graphics.Font()
        font.LoadFont(self.alert_font)
        textColor = graphics.Color(255, 255, 255)


        graphics.DrawText(matrix, font, 40, 10, graphics.Color(255, 255, 255), "ONE")
        
        #type of bird
        graphics.DrawText(matrix, font, pos, 20, graphics.Color(255, 255, 255), spotted_bird.bird_name)

        #location
        total_length = graphics.DrawText(matrix, font, pos, 30, textColor, spotted_bird.bird_loc)

        pos -= 1

        time.sleep(0.05)
        
        return pos, total_length
