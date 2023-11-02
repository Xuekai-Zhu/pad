def solution():
    """Marco loves trading cards. He has a total of 500 cards on hand, and a fourth of them are duplicates. Marco decides to trade one-fifth of these duplicates for completely new cards to his friend Josh. How many new cards did Marco get?"""
    # Define the total number of cards and the number of duplicate cards
    total_cards = 500
    duplicate_cards = total_cards / 4

    # Calculate the number of duplicate cards that Marco traded
    traded_cards = duplicate_cards / 5

    # Calculate the number of new cards Marco received in the trade
    new_cards = traded_cards

    # return the result
    result = new_cards
    return result

print(solution())