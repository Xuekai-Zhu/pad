def solution():
    """Matt has 8 baseball cards worth $6 each. If he trades two of them to Jane in exchange for 3 $2 cards and 1 $9 card, how much profit does he make?"""
    # Define the initial value of Matt's baseball cards
    initial_value = 8 * 6

    # Define the value of the cards he traded to Jane
    traded_value = 2 * 6

    # Define the value of the cards he received from Jane
    received_value = 3 * 2 + 9

    # Calculate the final value of his collection
    final_value = initial_value - traded_value + received_value

    # Calculate the profit he made
    profit = final_value - initial_value

    result = profit
    return result

print(solution())