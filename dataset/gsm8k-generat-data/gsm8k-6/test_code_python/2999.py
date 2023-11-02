def solution():
    # Calculate the number of white marbles
    white_marbles = 50 / 2

    # Calculate the number of green marbles
    green_marbles = 12 / 2

    # Calculate the total number of marbles without the red ones
    total_without_red = white_marbles + 12 + green_marbles

    # Calculate the number of red marbles
    red_marbles = 50 - total_without_red
    result = red_marbles
    return result

print(solution())