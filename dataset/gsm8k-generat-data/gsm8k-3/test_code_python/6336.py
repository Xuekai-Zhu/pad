def solution():
    """Marco loves trading cards. He has a total of 500 cards on hand, and a fourth of them are duplicates. Marco decides to trade one-fifth of these duplicates for completely new cards to his friend Josh. How many new cards did Marco get?"""
    # Determine the number of duplicate cards Marco has
    duplicates = 500 / 4

    # Determine the number of duplicates Marco wants to trade
    duplicates_to_trade = duplicates / 5

    # Determine the number of new cards Marco will receive in the trade
    new_cards = duplicates_to_trade

    # Display the number of new cards Marco received
    result = new_cards
    return result

print(solution())