def solution():
    # Calculate the initial value of Matt's baseball cards
    initial_value = 8 * 6  # 8 cards worth $6 each

    # Calculate the value of the items he traded for
    traded_value = 3 * 2 + 1 * 9  # 3 $2 cards and 1 $9 card

    # Calculate the final value of Matt's collection after the trade
    final_value = initial_value - 2 * 6 + traded_value  # traded 2 cards worth $6 each

    # Calculate the profit made by Matt
    profit = final_value - initial_value
    result = profit
    return result

print(solution())