
import random

class BattleshipBot:

    def __init__(self):
        pass

    def get_configuration(self):
        return [
            {
                "name": "Carrier",
                "size": 5,
                "squares": [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]
            },
            {
                "name": "Battleship",
                "size": 4,
                "squares": [[0, 1], [1, 1], [2, 1], [3, 1]]
            },
            {
                "name": "Cruiser",
                "size": 3,
                "squares": [[0, 2], [1, 2], [2, 2]]
            },
            {
                "name": "Submarine",
                "size": 3,
                "squares": [[0, 3], [1, 3], [2, 3]]
            },
            {
                "name": "Destroyer",
                "size": 2,
                "squares": [[0, 4], [1, 4]]
            }
        ]

    def get_move(self, grid):
        return random.randint(0, 7), random.randint(0, 7)
