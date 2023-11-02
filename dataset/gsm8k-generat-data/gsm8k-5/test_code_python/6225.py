def solution():
    jesus_squares = 60
    linden_squares = 75
    pedro_squares = 200

    # Calculate total squares for Jesus and Linden combined
    total_square_jl = jesus_squares + linden_squares

    # Calculate the difference between Pedro's squares and the total squares of Jesus and Linden combined
    difference = pedro_squares - total_square_jl
    result = difference
    return result

print(solution())