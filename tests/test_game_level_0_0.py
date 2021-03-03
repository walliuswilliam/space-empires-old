import sys
sys.path.append('players')
sys.path.append('game')
from custom_player import *
from random_player import *
from game_level_0_0 import *

players = [RandomPlayer(), CustomPlayer()]
game = Game(players)


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


game.complete_turn()
print(game.game_state)

# {
#     'turn': 2,
#     'board_size': [7,7],
#     'players': {
#         1: {
#             'scout_coords': (will vary),
#             'home_colony_coords': (4, 1)
#         },
#         2: {
#             'scout_coords': (4, 6),
#             'home_colony_coords': (4, 7)
#         }
#     },
#     'winner': None
# }

game.run_to_completion()
print('\n' + str(game.game_state))

# {
#     'turn': 7,
#     'board_size': [7,7],
#     'players': {
#         1: {
#             'scout_coords': (will vary),
#             'home_colony_coords': (4, 1)
#         },
#         2: {
#             'scout_coords': (4, 1),
#             'home_colony_coords': (4, 7)
#         }
#     },
#     'winner': 2
# }
