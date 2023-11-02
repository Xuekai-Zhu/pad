def solution():
    """Keith bought 8 new baseball trading cards to add to his collection. The next day his dog ate half of his collection. There are now only 46 cards left. How many cards did Keith start with?"""
    new_cards = 8
    remaining_cards = 46
    starting_cards = (remaining_cards + new_cards) * 2
    result = starting_cards
    return result

print(solution())