def solution():
    
    crossword_time = 10
    sudoku_time = 5
    num_crossword_puzzles = 3
    num_sudoku_puzzles = 8
    total_time = (crossword_time * num_crossword_puzzles) + (sudoku_time * num_sudoku_puzzles)
    result = total_time
    return result

print(solution())