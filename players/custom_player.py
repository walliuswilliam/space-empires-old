import math

class CustomPlayer():
  def __init__(self):
    self.player_number = None

  def set_player_number(self, n):
    self.player_number = n

  def get_opponent_player_number(self):
    if self.player_number == None:
      return None
    elif self.player_number == 1:
      return 2
    elif self.player_number == 2:
      return 1

  def choose_translation(self, game_state, choices, scout):
    myself = game_state['players'][self.player_number]
    opponent_player_number = self.get_opponent_player_number()
    opponent = game_state['players'][opponent_player_number]

    my_scout_coords = myself['scout_coords'][scout]
    opponent_home_colony_coords = opponent['home_colony_coords']

    best_move = choices[0]

    for choice in choices:
      choice_coords = (my_scout_coords[0]+choice[0], my_scout_coords[1]+choice[1])
      best_coords = (my_scout_coords[0]+best_move[0], my_scout_coords[1]+best_move[1])
      choice_distance = self.calc_distance(choice_coords, opponent_home_colony_coords)
      best_distance = self.calc_distance(best_coords, opponent_home_colony_coords)

      if choice_distance < best_distance:
        best_move = choice

    return best_move
  
  def calc_distance(self, point1, point2):
    return abs(math.sqrt((point2[0]-point1[0])**2+(point2[1]-point1[1])**2))
