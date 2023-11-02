def solution():
    
    normal_sudoku_time = 45
    animee_sudoku_time = normal_sudoku_time * 4
    normal_sudoku_bottles = normal_sudoku_time / 0.5
    animee_sudoku_bottles = animee_sudoku_time / 0.5
    total_bottles = normal_sudoku_bottles + animee_sudoku_bottles
    result = total_bottles
    return result

print(solution())