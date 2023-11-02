def solution():
    """Joseph had 16 baseball cards. He gave 3/8 of the cards to his brother and 2 cards to his brother. What percentage of the cards is left to Joseph?"""
    # Define the initial number of baseball cards
    initial_cards = 16

    # Calculate the number of cards Joseph gave to his brother
    brother_cards = initial_cards * 3/8 + 2

    # Calculate the number of cards Joseph has left
    remaining_cards = initial_cards - brother_cards

    # Calculate the percentage of cards Joseph has left
    percentage_left = (remaining_cards / initial_cards) * 100

    # Return the result
    result = percentage_left
    return result

print(solution())