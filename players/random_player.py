import math
from random import random

class RandomPlayer():
  def __init__(self):
    self.player_number = None

  def set_player_number(self, n):
    self.player_number = n

  def choose_translation(self, game_state, choices):
    random_idx = math.floor(len(choices) * random())
    return choices[random_idx]