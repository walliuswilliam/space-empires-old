import sys
sys.path.append('players')
sys.path.append('game')
from custom_player import *
from random_player import *
from game_level_0_1 import *


players = [CustomPlayer(), CustomPlayer()]
game = Game(players)
assert game.state['players'] == {
    1: {
        'scout_coords': (4, 1),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 7),
        'home_colony_coords': (4, 7)
    }
}

game.complete_movement_phase()
assert game.state['players'] == {
    1: {
        'scout_coords': (4, 2),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 6),
        'home_colony_coords': (4, 7)
    }
}

game.complete_combat_phase()

game.complete_movement_phase()
assert game.state['players'] == {
    1: {
        'scout_coords': (4, 3),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 5),
        'home_colony_coords': (4, 7)
    }
}

game.complete_combat_phase()

game.complete_movement_phase()
assert game.state['players'] == {
    1: {
        'scout_coords': (4, 4),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 4),
        'home_colony_coords': (4, 7)
    }
}

game.complete_combat_phase()


print(game.state['players'])
#There are two possible outcomes:
# Possibility 1:
{
    1: {
        'scout_coords': None,
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': (4, 4),
        'home_colony_coords': (4, 7)
    }
}

# Possibility 2:
{
    1: {
        'scout_coords': (4, 4),
        'home_colony_coords': (4, 1)
    },
    2: {
        'scout_coords': None,
        'home_colony_coords': (4, 7)
    }
}




num_wins = {1: 0, 2: 0}
for _ in range(200):
        players = [CustomPlayer(), CustomPlayer()]
        game = Game(players)
        game.run_to_completion()
        winner = game.state['winner']
        num_wins[winner] += 1
print(num_wins)


# num_wins
# Should be close (but probably not exactly equal) 
# to {1: 100, 2: 100}