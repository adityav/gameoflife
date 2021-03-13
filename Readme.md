# Game Of life

This commandline tool simulates game of life.

The algorithm is a 2 step process

1. Compute the number of living neighbours of a cell
2. using above, we apply rules to all cells where number of living neighbours > 0 to get the new generate

## Code

there are 2 main files

- gameoflife/gameboard.py - Manages state of the game. Tools to add a cell or pattern, print gameboard, compare
- gameoflife/gameoflife.py - The class containing the main algorithm


## Running

The project requires `pipenv` on PATH and python >= 3.7 to be available.
It install pipenv, follow https://docs.pipenv.org/en/latest/#install-pipenv-today

### Setup of environment
```
# install dependencies and setup pipenv
make init

# test code
make test
```

### Example run for the takehome

```
# pipenv run python driver.py 25 25 1 1 inputs/glider.txt
```

### Example run for a gosper glider gun
```
# pipenv run python driver.py 50 50 1 1 inputs/gosperglidergun.txt
```

### Full commandline help text
```
# pipenv run python driver.py --help
usage: driver.py [-h] maxrows maxcols offset_row offset_col inputfile

Simulate game of life using initial pattern.

positional arguments:
  maxrows     max number of rows for the gameboard
  maxcols     max number of cols for the gameboard
  offset_row  row number where pattern is spawned. defaults to 0
  offset_col  col number where pattern is spawned. defaults to 0
  inputfile   a file containing initial pattern

optional arguments:
  -h, --help  show this help message and exit
```
