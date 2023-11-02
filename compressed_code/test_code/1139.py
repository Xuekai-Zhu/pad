def solution():
    
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