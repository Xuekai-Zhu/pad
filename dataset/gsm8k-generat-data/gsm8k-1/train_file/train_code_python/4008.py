def solution():
    """Jim had 365 trading cards. He gives 8 sets of cards to his brother, 5 sets of cards to his sister, and 2 sets of cards to his friend. How many cards did he give away, assuming 1 set has 13 trading cards?"""
    total_cards = 365
    brother_sets = 8
    sister_sets = 5
    friend_sets = 2
    cards_per_set = 13
    total_given_away = (brother_sets + sister_sets + friend_sets) * cards_per_set
    result = total_given_away
    return result

print(solution())