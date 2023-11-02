def solution():
    single_points = 1000
    tetris_points = 8 * single_points
    
    num_singles = 6
    num_tetrises = 4
    
    # Calculate the total points from singles
    total_single_points = num_singles * single_points
    
    # Calculate the total points from tetrises
    total_tetris_points = num_tetrises * tetris_points
    
    # Calculate the total points Tim scored
    total_points = total_single_points + total_tetris_points
    result = total_points
    return result

print(solution())