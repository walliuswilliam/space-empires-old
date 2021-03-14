import sys
sys.path.append('players')
sys.path.append('logs')
from custom_player import *
from random_player import *
from logger import *
import random

class Game:
  def __init__(self, players, random_seed=random.random(), board_size=[7,7]):
    self.players = players
    self.set_player_numbers()
    self.log = Logger('log_0_2.txt')
    self.log.clear_log()

    
    # random.seed(random_seed)
    # self.random_int = 3-(round(random.random()) + 1)

    board_x, board_y = board_size
    mid_x = (board_x + 1) // 2
    mid_y = (board_y + 1) // 2

    self.state = {
      'turn': 1,
      'board_size': board_size,
      'players': {
        1: {
            'scout_coords': {
                1: (mid_x, 1),
                2: (mid_x, 1),
                3: (mid_x, 1),
            },
            'home_colony_coords': (mid_x, 1)
        },
        2: {
            'scout_coords': {
                1: (mid_x, 7),
                2: (mid_x, 7),
                3: (mid_x, 7),
            },
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
    board_x, board_y = self.state['board_size']
    if 1 <= x and x <= board_x:
      if 1 <= y and y <= board_y:
        return True
    return False

  def check_if_translation_is_in_bounds(self, coords, translation):
      max_x, max_y = self.state['board_size']
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

  def complete_movement_phase(self):
    self.log.write('\nBEGINNING OF TURN {} MOVEMENT PHASE\n\n'.format(self.state['turn']))
    for player in self.players:
      for scout_key in self.get_scout_coords(player.player_number):
        if self.check_if_on_same_spot(scout_key, self.get_opposite_player_number(player.player_number)) is False:
          player_scout_coords = self.get_scout_coords(player.player_number)[scout_key]
          choices = self.get_in_bounds_translations(player_scout_coords)
          turn = player.choose_translation(self.state, choices, scout_key)
          new_coords = (player_scout_coords[0]+turn[0], player_scout_coords[1]+turn[1])
          
          self.log.write('\tPlayer {} Scout {}: {} -> {}\n'.format(player.player_number, scout_key, player_scout_coords, new_coords))

          self.state['players'][player.player_number]['scout_coords'][scout_key] = new_coords
        else:
          None
    self.log.write('\nEND OF TURN {} MOVEMENT PHASE\n'.format(self.state['turn']))
      
  def complete_combat_phase(self):
    self.log.write('\nBEGINNING OF TURN {} COMBAT PHASE\n'.format(self.state['turn']))
    scouts_combat = self.check_if_any_on_same_spot()
    if scouts_combat is not None:      
      self.log.write('\n\tCombat at {}\n'.format(self.state['players'][1]['scout_coords'][scouts_combat[1]]))
    while self.check_if_any_on_same_spot() is not None:
      scouts_combat = self.check_if_any_on_same_spot()
      random_player = random.randint(1,2)
      del self.state['players'][random_player]['scout_coords'][scouts_combat[random_player]]
      self.log.write('\n\t\t Player {} Scout {} was destroyed.'.format(random_player, scouts_combat[random_player]))
    self.log.write('\n\nEND OF TURN {} COMBAT PHASE\n'.format(self.state['turn']))

  def check_winner(self):
    game_players = self.state['players']
    winners = []
    for scout_1 in self.get_scout_coords(1).values():
      if scout_1 == game_players[2]['home_colony_coords']:
        self.state['winner'] = 1
        break
    for scout_2 in self.get_scout_coords(2).values():
      if scout_2 == game_players[1]['home_colony_coords']:
        self.state['winner'] = 2
        break

  
  def run_to_completion(self, max_turns = 999999999):
    self.check_winner
    while self.state['winner'] is None and self.state['turn'] <= max_turns:
      self.complete_movement_phase()
      self.complete_combat_phase()
      self.check_winner()
      self.state['turn'] += 1





  #HELPER FUNCTIONS
  def get_scout_coords(self, player_number):
    return self.state['players'][player_number]['scout_coords']

  def get_scout_coords_at_key(self, player_number, key):
    return self.state['players'][player_number]['scout_coords'][key]

  def check_if_any_on_same_spot(self):
    for player_1_scout_key in self.get_scout_coords(1):
      for player_2_scout_key in self.get_scout_coords(2):
        if self.get_scout_coords_at_key(1, player_1_scout_key) == self.get_scout_coords_at_key(2, player_2_scout_key):
          return {1: player_1_scout_key, 2: player_2_scout_key}
    return None

  def check_if_on_same_spot(self, scout_key, player_to_compare):
    for compare_scout_key in self.get_scout_coords(player_to_compare):
      if self.get_scout_coords_at_key(player_to_compare, compare_scout_key) == self.get_scout_coords_at_key(self.get_opposite_player_number(player_to_compare), scout_key):
        return True
    else:
      return False

    
  def get_opposite_player_number(self, player_number):
    if player_number == None:
      return None
    elif player_number == 1:
      return 2
    elif player_number == 2:
      return 1

