def solution():
    """Keith bought 8 new baseball trading cards to add to his collection. The next day his dog ate half of his collection. There are now only 46 cards left. How many cards did Keith start with?"""
    # Define the number of new baseball cards Keith bought
    new_cards = 8

    # Define the current number of baseball cards after his dog ate half of his collection
    current_cards = 46

    # Calculate the number of cards before his dog ate half of his collection
    original_cards = current_cards * 2 + new_cards

    # Return the result
    result = original_cards
    return result

print(solution())