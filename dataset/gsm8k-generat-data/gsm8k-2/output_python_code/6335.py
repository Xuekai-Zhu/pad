def solution():
    """Marco loves trading cards. He has a total of 500 cards on hand, and a fourth of them are duplicates. Marco decides to trade one-fifth of these duplicates for completely new cards to his friend Josh. How many new cards did Marco get?"""
    total_cards = 500
    duplicates = total_cards / 4
    traded_duplicates = duplicates / 5
    new_cards = traded_duplicates
    result = new_cards
    return result

print(solution())