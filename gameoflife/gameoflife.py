"""Game of Life algorithm
"""
import logging
from collections import defaultdict
from .gameboard import GameBoard

log = logging.getLogger(__name__)


class GameOfLife:
    def __init__(self, initial_gameboard: GameBoard):
        self.gameboard = initial_gameboard

    def simulate(self):
        """runs the game of life for 1 cycle
        It is a 2 step process
        1) count the number of living neighbours for a cell
        2) using above, apply rules to figure out which cells will live in next generation
        """
        init_state = self.gameboard

        # step 1: count the number of living neighbours for a cell
        count_alive_neighbours = self.count_alive_neighbours(init_state)

        # step 2: now we apply the rules to get the next gameboard
        next_state = self.apply_rules(init_state, count_alive_neighbours)

        self.gameboard = next_state
        return self

    def count_alive_neighbours(self, state: GameBoard) -> dict:
        """Returns a dict which contains the count of number of living neighbours of a cell

        dict[(row, col)] is the count of neighbours for cell(row, col)
        """
        count_neighbours = defaultdict(int)
        for cell in state.cells:
            # explore the 8 directions
            for offset_row in [-1, 0, 1]:
                for offset_col in [-1, 0, 1]:
                    if offset_row == 0 and offset_col == 0:
                        continue
                    row = cell[0] + offset_row
                    col = cell[1] + offset_col
                    if state.is_valid_cell(row, col):
                        count_neighbours[(row, col)] += 1
        return count_neighbours

    def apply_rules(self, state: GameBoard, count_alive_neighbours: dict):
        """Apply the rules of the game and generate the new gameboard"""
        next_state = state.empty_board()
        for (row, col), count in count_alive_neighbours.items():
            if state.is_alive(row, col):
                if count == 2 or count == 3:
                    log.debug("(%s, %s) continues living", row, col)
                    next_state.add(row, col)
                else:
                    log.debug("(%s, %s) dies", row, col)
            else:
                if count == 3:
                    log.debug("(%s, %s) is born", row, col)
                    next_state.add(row, col)
        return next_state

    def simulate_n(self, num_gens: int = 1):
        """Simulate the game for given number of iterations"""
        for i in range(num_gens):
            self.simulate()
            log.info("Generation: %s", 1 + i)
            self.gameboard.display()

        return self

    def display(self):
        self.gameboard.display()

    def print_board(self):
        self.gameboard.print_board()
