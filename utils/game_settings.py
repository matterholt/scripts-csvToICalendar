from dataclasses import dataclass

@dataclass
class GameSettings:
  division : str
  duration : int


lollipop = GameSettings(division="lollipop", duration=4*8)
wing = GameSettings(division="wing", duration=4*12)
striker = GameSettings(division="striker", duration=4*15)
