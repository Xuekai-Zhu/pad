def solution():
    """A single line is worth 1000 points.  A tetris is worth 8 times that much.   Tim scored 6 singles and 4 tetrises.  How many points did he score?"""
    # Define the point values
    SINGLE_VALUE = 1000
    TETRIS_VALUE = SINGLE_VALUE * 8

    # Define the number of singles and tetrises scored by Tim
    singles = 6
    tetrises = 4

    # Calculate Tim's total score
    total_score = (singles * SINGLE_VALUE) + (tetrises * TETRIS_VALUE)

    # Display Tim's total score
    result = total_score
    return result

print(solution())