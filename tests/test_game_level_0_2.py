import sys
sys.path.append('players')
sys.path.append('game')
from custom_player import *
from random_player import *
from game_level_0_2 import *


# tests = [
#     {'seed': 0, 'winner': 2},
#     {'seed': 1, 'winner': 1},
#     {'seed': 2, 'winner': 2},
#     {'seed': 3, 'winner': 1},
#     {'seed': 4, 'winner': 1},
#     {'seed': 5, 'winner': 2},
#     {'seed': 6, 'winner': 2},
#     {'seed': 7, 'winner': 1},
#     {'seed': 8, 'winner': 1},
#     {'seed': 9, 'winner': 1}
# ]

# print('testing random winner...')
# for test in tests:
#     players = [CustomPlayer(), CustomPlayer()]
#     random_seed = test['seed']

#     game = Game(players, random_seed)
#     game.run_to_completion()

#     desired_winner = test['winner']
#     assert(game.state['winner'] == desired_winner)
# print('passed')


num_wins = {1: 0, 2: 0}
scouts_remaining = {1: 0, 2: 0}
for _ in range(200):
  players = [CustomPlayer(), CustomPlayer()]
  game = Game(players)
  game.run_to_completion()
  winner = game.state['winner']
  scouts_remaining[winner] += len(game.state['players'][winner]['scout_coords'])
  num_wins[winner] += 1
avg_scouts_remaining = {k:v/200 for k,v in scouts_remaining.items()}

print(num_wins)
print(avg_scouts_remaining)


# logger = Logger('/home/runner/space-empires/logs/silly-log.txt')
# logger.write('stuff')