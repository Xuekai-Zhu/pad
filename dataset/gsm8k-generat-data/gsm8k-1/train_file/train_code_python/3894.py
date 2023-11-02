def solution():
    """Joseph had 16 baseball cards. He gave 3/8 of the cards to his brother and 2 cards to his brother. What percentage of the cards is left to Joseph?"""
    total_cards = 16
    given_cards = (3/8)*total_cards + 2
    left_cards = total_cards - given_cards
    percentage_left = (left_cards / total_cards) * 100
    result = percentage_left
    return result

print(solution())