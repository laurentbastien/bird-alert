import time

from rgbmatrix import graphics


class Alerts:
    def __init__(self, alert_font):
        self.alert_font = alert_font

    @staticmethod
    def __parse_date(spotted_bird):
        time_of_spot = spotted_bird.date

        return "{}|{}|{}".format(
            time_of_spot.day, time_of_spot.month, str(time_of_spot.year)[2:]
        )

    @staticmethod
    def __clean_scroll(bird_length, bird_loc):
        if bird_length > bird_loc:
            return bird_length
        return bird_loc

    def __load_font(self):
        font = graphics.Font()
        font.LoadFont(self.alert_font)

        return font

    def set_alerts(self, matrix, pos, spotted_bird):
        font = self.__load_font()
        bird_time = self.__parse_date(spotted_bird)
        textColor = graphics.Color(255, 255, 255)

        # time of spot
        graphics.DrawText(matrix, font, 32, 7, graphics.Color(255, 255, 255), bird_time)

        # type of bird
        bird_length = graphics.DrawText(
            matrix, font, pos, 20, graphics.Color(255, 255, 255), spotted_bird.bird_name
        )

        # location
        bird_loc = graphics.DrawText(
            matrix, font, pos, 30, textColor, spotted_bird.bird_loc
        )

        pos -= 1

        time.sleep(0.05)

        total_length = self.__clean_scroll(bird_length, bird_loc)

        return pos, total_length
