def solution():
    """Joseph had 16 baseball cards. He gave 3/8 of the cards to his brother and 2 cards to his brother. What percentage of the cards is left to Joseph?"""
    # Define the initial number of cards
    initial_cards = 16

    # Calculate the number of cards given to Joseph's brother
    brother_cards = (3/8) * initial_cards + 2

    # Calculate the number of cards left with Joseph
    left_cards = initial_cards - brother_cards

    # Calculate the percentage of cards left with Joseph
    percentage_left = (left_cards / initial_cards) * 100

    # Display the percentage of cards left with Joseph
    result = percentage_left
    return result

print(solution())