def solution():
    # Calculate the square footage of each painting
    square_footage_6ft = 6 * 6
    square_footage_2ft = 2 * 3
    square_footage_10ft = 10 * 15

    # Calculate the total square footage of the art collection
    total_square_footage = (3 * square_footage_6ft) + (4 * square_footage_2ft) + square_footage_10ft
    result = total_square_footage
    return result

print(solution())