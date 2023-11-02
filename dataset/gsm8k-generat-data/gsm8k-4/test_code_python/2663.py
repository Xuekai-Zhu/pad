def solution():
    """Nicky is trading baseball cards with Jill. If Nicky trades two cards worth $8 each for 1 card worth $21, how many dollars of profit does he make?"""
    # Calculate the total value of the traded cards
    total_value_traded = 2 * 8

    # Calculate the value of the card received in exchange
    received_value = 21

    # Calculate the profit made in the trade
    profit = received_value - total_value_traded

    result = profit
    return result

print(solution())