import sys
sys.path.append('src')
from game_level_0_0 import Game
from game_level_0_0 import RandomPlayer
from game_level_0_0 import CustomPlayer



players = [RandomPlayer(), CustomPlayer()]
game = Game(players)


def random_remover(input_dict):
  output_dict = input_dict.copy()
  del output_dict['players'][1]
  return output_dict


assert game.game_state == {
    'turn': 1,
    'board_size': [7,7],
    'players': {
        1: {
            'scout_coords': (4, 1),
            'home_colony_coords': (4, 1)
        },
        2: {
            'scout_coords': (4, 7),
            'home_colony_coords': (4, 7)
        }
    },
    'winner': None
}

print('testing complete_turn...')
game.complete_turn()
assert random_remover(game.game_state) == {
    'turn': 2,
    'board_size': [7,7],
    'players': {
        2: {
            'scout_coords': (4, 6),
            'home_colony_coords': (4, 7)
        }
    },
    'winner': None
}, game.game_state
print('passed')

print('testing run_to_completion...')
game.run_to_completion()
print(game.game_state)
assert random_remover(game.state) == {
    'turn': 7,
    'board_size': [7,7],
    'players': {
        2: {
            'scout_coords': (4, 1),
            'home_colony_coords': (4, 7)
        }
    },
    'winner': 2
}
print('passed')



