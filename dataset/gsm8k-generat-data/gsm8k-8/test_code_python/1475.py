def solution():
    # Calculate the number of blue marbles
    blue_marbles = 0.4 * 10

    # Calculate the number of red marbles
    red_marbles = 10 - blue_marbles - 1

    # Calculate the number of marbles after the trade
    traded_blue = 2 * (red_marbles - 1)
    remaining_blue = blue_marbles - traded_blue
    total_marbles = remaining_blue + red_marbles + 1

    result = total_marbles
    return result

print(solution())