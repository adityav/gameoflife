import argparse
import logging
from gameoflife.gameoflife import GameOfLife
from gameoflife.gameboard import GameBoard


log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def extract_pattern(inputfile):
    """loads pattern from the file.

    Arguments:
        inputfile {file} -- file containing pattern

    Returns:
        List[Tuple(int,int)] -- A list of coordinates
    """
    pattern = []
    current_row = 0
    for line in inputfile:
        if line.startswith("!"):
            continue
        line = line.strip()

        for col, ch in enumerate(line):
            if ch == '1' or ch == 'O':
                pattern.append((current_row, col))

        current_row += 1
    return pattern


def main():
    parser = argparse.ArgumentParser(description='Simulate game of life using initial pattern.')
    parser.add_argument('maxrows', type=int, help="max number of rows for the gameboard")
    parser.add_argument('maxcols', type=int, help="max number of cols for the gameboard")
    parser.add_argument('offset_row', type=int, help="row number where pattern is spawned. defaults to 0")
    parser.add_argument('offset_col', type=int, help="col number where pattern is spawned. defaults to 0")
    parser.add_argument(
        'inputfile', type=open,
        help='a file containing initial pattern')

    args = parser.parse_args()
    pattern = extract_pattern(args.inputfile)

    gameboard = GameBoard(args.maxrows, args.maxcols)
    gameboard.add_pattern(pattern, (args.offset_row,args.offset_col))
    log.info("Initializing gameboard of size %sx%s", args.maxrows, args.maxcols)
    log.info("pattern spawned at (%s,%s)", args.offset_row, args.offset_col)
    gameboard.print_board()

    game = GameOfLife(gameboard)
    print("Begin game")
    while True:
        game.simulate()
        game.print_board()
        inp = input("Press enter to generate next iteration...")

if __name__ == "__main__":
    main()
