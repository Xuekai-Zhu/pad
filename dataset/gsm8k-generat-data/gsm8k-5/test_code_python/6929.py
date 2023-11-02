def solution():
    # Calculate the initial value of Matt's baseball cards
    initial_value = 8 * 6  # 8 cards worth $6 each

    # Calculate the value of the cards he traded
    traded_value = 2 * 6  # 2 cards worth $6 each

    # Calculate the value of the cards he received in exchange
    received_value = (3 * 2) + 9  # 3 $2 cards and 1 $9 card

    # Calculate the total value after the trade
    total_value = initial_value - traded_value + received_value

    # Calculate the profit made from the trade
    profit = total_value - initial_value
    result = profit
    return result

print(solution())