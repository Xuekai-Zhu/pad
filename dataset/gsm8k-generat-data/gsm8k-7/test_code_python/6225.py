def solution():
    jesus_squares = 60
    linden_squares = 75
    pedro_squares = 200

    # Calculate the total number of squares that Jesus and Linden combined have
    combined_squares = jesus_squares + linden_squares

    # Calculate the number of more squares that Pedro has than Jesus and Linden combined
    more_squares = pedro_squares - combined_squares
    result = more_squares
    return result

print(solution())