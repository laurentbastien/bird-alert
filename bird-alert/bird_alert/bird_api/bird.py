from dataclasses import dataclass
from datetime import datetime

@dataclass()
class Bird:
    bird_name: str
    bird_loc: str
    how_many: int
    date: datetime
