def solution():
    # Calculate the amount of money Tom received for trading in his Super Nintendo
    trade_in_value = 0.8 * 150  # the store gives him 80% of the value of the SNES

    # Calculate the total cost of the NES and the game
    total_cost = trade_in_value + 80 - 10 + 30  # he gives $80, gets $10 change, and adds a $30 game to the trade-in value

    result = total_cost
    return result

print(solution())