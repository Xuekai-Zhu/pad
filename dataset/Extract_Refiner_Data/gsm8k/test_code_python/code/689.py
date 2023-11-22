def solution():
    
    red_squares = 14
    blue_squares = red_squares + 4
    green_squares = blue_squares + 6
    white_squares = green_squares - 12
    total_square_feet = (red_squares * 1) + (blue_squares * 1) + (green_squares * 1) + (white_squares * 1)
    result = total_square_feet
    return result

print(solution())