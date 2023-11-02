def solution():
    # Calculate the area of the three square 6ft x 6ft paintings
    square_area = 6*6
    total_square_area = 3 * square_area

    # Calculate the area of the four 2ft x 3ft paintings
    small_area = 2*3
    total_small_area = 4 * small_area

    # Calculate the area of the one large 10ft x 15ft painting
    large_area = 10*15

    # Calculate the total area of the art collection
    total_area = total_square_area + total_small_area + large_area
    result = total_area
    return result

print(solution())