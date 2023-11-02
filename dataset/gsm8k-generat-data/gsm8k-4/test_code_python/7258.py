def solution():
    """A single line is worth 1000 points. A tetris is worth 8 times that much. Tim scored 6 singles and 4 tetrises. How many points did he score?"""
    # Define the value of a single line and a tetris
    SINGLE_VALUE = 1000
    TETRIS_VALUE = SINGLE_VALUE * 8

    # Calculate Tim's score
    singles_score = 6 * SINGLE_VALUE
    tetrises_score = 4 * TETRIS_VALUE
    total_score = singles_score + tetrises_score

    # return the result
    result = total_score
    return result

print(solution())