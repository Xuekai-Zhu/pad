def solution():
    """Nicky is trading baseball cards with Jill. If Nicky trades two cards worth $8 each for 1 card worth $21, how many dollars of profit does he make?"""
    # Define the value of each card
    CARD_VALUE = 8

    # Calculate the cost of the two cards Nicky trades
    cost = 2 * CARD_VALUE

    # Calculate the value of the card Nicky receives in the trade
    value = 21

    # Calculate the profit Nicky makes
    profit = value - cost

    # Display the profit
    result = profit
    return result

print(solution())