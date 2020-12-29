from typing import List

from dateutil import parser
from ebird.api import get_nearby_notable, get_nearby_observations

from bird_alert.bird_api.bird import Bird

LAT = 45.53512894561012
LONG = -73.60905912519931
DIST = 5
SINCE = 2


class BirdClient:
    def __init__(self, client_token):
        self.client_token = client_token

    @staticmethod
    def __parse_records(records: List):
        record = records[0]
        return Bird(
            bird_name=record["comName"],
            bird_loc=record["locName"],
            how_many=record["howMany"],
            date=parser.parse(record["obsDt"]),
        )

    def fetch_nearby_rare(self):
        records = get_nearby_notable(self.client_token, LAT, LONG, DIST)
        bird_found = self.__parse_records(records)
        return bird_found

    def fetch_nearby_observed(self):
        records = get_nearby_observations(self.client_token, LAT, LONG, DIST, SINCE)
        bird_found = self.__parse_records(records)
        return bird_found
