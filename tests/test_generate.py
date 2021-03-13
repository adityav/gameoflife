from gameoflife.gameoflife import GameBoard, GameOfLife


def test_pattern():
    """Check if the bar pattern switches between horizontal and vertical alignment
    """
    pattern = [(0,0),(0,1),(0,2)]
    test_pattern = [(0,0), (1,0), (2,0)]

    gameboard = GameBoard(5, 5)
    gameboard.add_pattern(pattern, (2,1))
    print("Initial pattern")
    gameboard.display()

    game = GameOfLife(gameboard)
    game.simulate_n(1)

    # check if bar has flipped to vertical alignment
    test_board = GameBoard(5, 5)
    test_board.add_pattern(test_pattern, (1,2))
    assert game.gameboard == test_board

    game.simulate_n(1)

    # check if bar is back to horizontal alignment
    test_board = GameBoard(5, 5)
    test_board.add_pattern(pattern, (2,1))
    assert game.gameboard == test_board


def test_takehome():
    """Test if the glider has gone through 1 full rotation
    """
    pattern = [
        (0,1),
        (1,2),
        (2,0),(2,1),(2,2)
    ]
    gameboard = GameBoard(25, 25)
    gameboard.add_pattern(pattern, (0,0))
    gameboard.display()

    game = GameOfLife(gameboard)
    game.simulate_n(4)

    test_board = GameBoard(25, 25)
    test_board.add_pattern(pattern, (1,1))
    assert game.gameboard == test_board
