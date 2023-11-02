def solution():
    total_marbles = 10
    blue_marbles = total_marbles * 0.4
    red_marbles = total_marbles - blue_marbles
    traded_marbles = red_marbles * 2
    total_after_trade = blue_marbles + traded_marbles
    result = total_after_trade
    return result

print(solution())