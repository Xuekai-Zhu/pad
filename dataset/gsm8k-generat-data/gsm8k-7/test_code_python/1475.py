def solution():
    total_marbles = 10
    blue_percentage = 0.40
    red_percentage = 1 - blue_percentage

    # Calculate the number of blue marbles
    num_blue_marbles = round(total_marbles * blue_percentage)

    # Calculate the number of red marbles
    num_red_marbles = total_marbles - num_blue_marbles

    # Keep one red marble and trade the rest for blue
    num_blue_marbles_from_trading = 2 * (num_red_marbles - 1)
    num_red_marbles_left = 1

    # Calculate the total number of marbles after trading
    total_marbles_after_trading = num_blue_marbles + num_red_marbles_left + num_blue_marbles_from_trading

    result = total_marbles_after_trading
    return result

print(solution())