def solution():
    square1 = 8 * 5
    square2 = 10 * 7
    square3 = 5 * 5
    total_square_feet = square1 + square2 + square3
    flag_length = 15
    flag_height = total_square_feet / flag_length
    result = flag_height
    
    return result

print(solution())