def solution():
    """Pete has a bag with 10 marbles. 40% are blue and the rest are red. His friend will trade him two blue marbles for every red one. If Pete keeps 1 red marble, how many total marbles does he have after trading with his friend?"""
    total_marbles = 10
    blue_marbles = total_marbles * 0.4
    red_marbles = total_marbles - blue_marbles
    traded_blue_marbles = 2 * (red_marbles - 1)
    new_blue_marbles = blue_marbles + traded_blue_marbles
    new_red_marbles = 1
    total_after_trading = new_blue_marbles + new_red_marbles
    result = total_after_trading
    return result

print(solution())