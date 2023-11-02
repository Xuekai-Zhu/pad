def solution():
    """Matt has 8 baseball cards worth $6 each. If he trades two of them to Jane in exchange for 3 $2 cards and 1 $9 card, how much profit does he make?"""
    # Define the worth of each baseball card and the number of cards Matt has
    CARD_WORTH = 6
    NUM_CARDS = 8

    # Calculate the initial value of Matt's cards
    initial_value = CARD_WORTH * NUM_CARDS

    # Calculate the value of the cards he traded for
    traded_value = 3*2 + 9

    # Calculate the new value of his card collection
    new_value = initial_value - 2*CARD_WORTH + traded_value

    # Calculate the profit he made
    profit = new_value - initial_value

    # Display the profit
    result = profit
    return result

print(solution())