def solution():
    # Calculate the number of blue marbles and red marbles
    blue_marbles = 0.4 * 10  # 40% of the marbles are blue
    red_marbles = 10 - blue_marbles  # the rest of the marbles are red

    # Calculate the number of blue marbles Pete will trade and the number of red marbles he will keep
    traded_blue = blue_marbles  # Pete can trade all of his blue marbles
    kept_red = 1  # Pete keeps 1 red marble

    # Calculate the total number of marbles Pete will have after trading
    total_marbles = traded_blue * 2 + kept_red + (10 - blue_marbles - kept_red)  # Pete trades 2 blue marbles for every red one
    result = total_marbles
    return result

print(solution())