"""Gameboard manages the state for simulating game of life
"""
import logging
from typing import List, Tuple

log = logging.getLogger(__name__)


class GameBoard:
    def __init__(self, maxrows: int, maxcols: int):
        self.cells = set()
        self.maxrows = maxrows
        self.maxcols = maxcols

    def is_alive(self, row: int, col: int) -> bool:
        """Returns True if the cell at (row,col) is alive"""
        return (row, col) in self.cells

    def is_valid_cell(self, row: int, col: int) -> bool:
        """Check if the cell(row,col) falls inside the gameboard boundaries"""
        return 0 <= row < self.maxrows and 0 <= col < self.maxcols

    def add(self, row: int, col: int):
        """mark cell(row, col) as living"""
        self.cells.add((row, col))
        return self

    def add_pattern(self, pattern: List[Tuple[int, int]], offset: Tuple[int, int]):
        """Add a pattern to the gameboard at the given offset"""
        for row, col in pattern:
            self.add(row + offset[0], col + offset[1])

    def empty_board(self):
        return GameBoard(self.maxrows, self.maxcols)

    def display(self):
        for i in range(self.maxrows):
            row = []
            for j in range(self.maxcols):
                disp = "1" if self.is_alive(i, j) else "0"
                row.append(disp)
            log.info(" ".join(row))

    def print_board(self):
        for i in range(self.maxrows):
            row = []
            for j in range(self.maxcols):
                disp = "1" if self.is_alive(i, j) else " "
                row.append(disp)
            print(" ".join(row))

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, GameBoard):
            return (
                self.maxrows == other.maxrows
                and self.maxcols == other.maxcols
                and self.cells == other.cells
            )
        return False
