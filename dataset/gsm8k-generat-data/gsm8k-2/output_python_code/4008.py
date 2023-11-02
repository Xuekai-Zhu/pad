def solution():
    """Jim had 365 trading cards. He gives 8 sets of cards to his brother, 5 sets of cards to his sister, and 2 sets of cards to his friend. How many cards did he give away, assuming 1 set has 13 trading cards?"""
    total_sets_given = 8 + 5 + 2
    cards_per_set = 13
    total_cards_given = total_sets_given * cards_per_set
    result = total_cards_given
    return result

print(solution())