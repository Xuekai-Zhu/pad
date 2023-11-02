def solution():
    """It takes Carmen 10 minutes to finish a crossword puzzle and 5 minutes to finish a sudoku puzzle. Over the weekend she solved 3 crossword puzzles and 8 sudoku puzzles. How much time did she spend playing these games?"""
    time_per_crossword = 10
    time_per_sudoku = 5
    num_crosswords = 3
    num_sudokus = 8
    total_time = (time_per_crossword * num_crosswords) + (time_per_sudoku * num_sudokus)
    result = total_time
    return result

print(solution())