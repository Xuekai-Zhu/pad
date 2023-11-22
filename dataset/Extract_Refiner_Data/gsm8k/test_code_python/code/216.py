def solution():
    
    # Define the time it takes to finish a crossword puzzle and a sudoku puzzle
    crossword_time = 10
    sudoku_time = 5

    # Define the number of crossword and sudoku puzzles solved
    num_crossword = 3
    num_sudoku = 8

    # Calculate the total time spent playing the games
    total_time = (crossword_time * num_crossword) + (sudoku_time * num_sudoku)

    # return the result
    result = total_time
    return result

print(solution())