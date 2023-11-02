def solution():
    
    red_squares = 14
    blue_squares = red_squares + 4
    green_squares = blue_squares + 6
    white_squares = green_squares - 12
    total_squares = red_squares + blue_squares + green_squares + white_squares
    result = total_squares
    return result

print(solution())