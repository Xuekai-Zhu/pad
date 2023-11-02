def solution():
    num_rows = 10 
    num_squares_per_row = 15
    num_red_rows = 4 
    num_red_squares_per_row = 6 
    num_green_rows = num_rows - num_red_rows
    num_green_squares_per_row = num_squares_per_row - num_red_squares_per_row
    total_num_green_squares = num_green_rows * num_green_squares_per_row
    result = total_num_green_squares 
    return result

print(solution())