def solution():
    # Define the number of white and yellow marbles
    white_marbles = 25
    yellow_marbles = 12

    # Calculate the number of green marbles, 50% fewer than yellow
    green_marbles = yellow_marbles * 0.5

    # Calculate the total number of marbles
    total_marbles = white_marbles + yellow_marbles + green_marbles + red_marbles

    # Calculate the number of red marbles, the remaining ones
    red_marbles = 50 - total_marbles

    result = red_marbles
    return result

print(solution())