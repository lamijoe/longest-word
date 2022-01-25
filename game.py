import random
import string
class Game():
    def __init__(self) -> None:
        self.grid = []
        for l in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
        
    def test_grid(grid):
        pass
    