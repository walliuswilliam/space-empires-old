from random import random
import math

class Game:
  def __init__(self, players, board_size=[7,7]):
    self.players = players
    self.set_player_numbers()

    board_x, board_y = board_size
    mid_x = (board_x + 1) // 2
    mid_y = (board_y + 1) // 2

    self.game_state = {
      'turn': 1,
      'board_size': board_size,
      'players': {
        1: {
          'scout_coords': (mid_x, 1),
          'home_colony_coords': (mid_x, 1)
        },
        2: {
          'scout_coords': (mid_x, board_y),
          'home_colony_coords': (mid_x, board_y)
        }
      },
      'winner': None
    }

  def set_player_numbers(self):
    for i, player in enumerate(self.players):
      player.set_player_number(i+1)

  def check_if_coords_are_in_bounds(self, coords):
    x, y = coords
    board_x, board_y = self.game_state['board_size']
    if 1 <= x and x <= board_x:
      if 1 <= y and y <= board_y:
        return True
    return False

  def check_if_translation_is_in_bounds(self, coords, translation):
      max_x, max_y = self.game_state['board_size']
      x, y = coords
      dx, dy = translation
      new_coords = (x+dx,y+dy)
      return self.check_if_coords_are_in_bounds(new_coords)

  def get_in_bounds_translations(self, coords):
    translations = [(0,0), (0,1), (0,-1), (1,0), (-1,0)]
    in_bounds_translations = []
    for translation in translations:
      if self.check_if_translation_is_in_bounds(coords, translation):
        in_bounds_translations.append(translation)
    return in_bounds_translations

  def complete_turn(self):
    for player in self.players:
      player_scout_coords = self.game_state['players'][player.player_number]['scout_coords']
      choices = self.get_in_bounds_translations(player_scout_coords)
      turn = player.choose_translation(self.game_state, choices)
      player_scout_coords = (player_scout_coords[0]+turn[0], player_scout_coords[1]+turn[1])
      
  def check_winner(self):
    game_players = self.game_state['players']
    winner = self.game_state['winner']
    winners = []
    if game_players[1]['scout_coords'] == game_players[2]['home_colony_coords']:
      winners.append(1)
    if game_players[2]['scout_coords'] == game_players[1]['home_colony_coords']:
      winners.append(2)
    if len(winners) == 2:
      winner = 'Tie'
    elif len(winners) == 1:
      winner = winners[0]
  
  def run_to_completion(self):
    self.check_winner
    while self.game_state['winner'] is None:
      self.complete_turn()
      self.check_winner()



class RandomPlayer():
  def __init__(self):
    self.player_number = None

  def set_player_number(self, n):
    self.player_number = n

  def choose_translation(self, game_state, choices):
    random_idx = math.floor(len(choices) * random())
    return choices[random_idx]


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

  def choose_translation(self, game_state, choices):
    myself = game_state['players'][self.player_number]
    opponent_player_number = self.get_opponent_player_number()
    opponent = game_state['players'][opponent_player_number]

    my_scout_coords = myself['scout_coords']
    opponent_home_colony_coords = opponent['home_colony_coords']

    best_move = choices[0]
    print('pre best move', best_move)
    print(choices)
    for choice in choices:
      
      if self.calc_distance(choice, opponent_home_colony_coords) < self.calc_distance(best_move, opponent_home_colony_coords):
        best_move = choice
    print(best_move)
    return best_move
  
  def calc_distance(self, point1, point2):
    return abs(math.sqrt((point2[0]-point1[0])**2+(point2[1]-point1[1])**2))
