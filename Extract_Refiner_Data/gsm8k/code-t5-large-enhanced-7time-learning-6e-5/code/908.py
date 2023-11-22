def solution():
    
    normal_sudoku_time = 45 / 60
    extreme_sudoku_time = 4 * normal_sudoku_time
    total_time = normal_sudoku_time + extreme_sudoku_time
    bottles_per_half_hour = 1 / 0.5
    total_bottles = total_time * bottles_per_half_hour
    result = total_bottles
    return result

print(solution())