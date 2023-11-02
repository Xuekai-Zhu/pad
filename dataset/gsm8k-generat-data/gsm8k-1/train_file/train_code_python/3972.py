def solution():
    """Jenny has 6 Pokemon cards. Orlando has 2 more cards than Jenny. Richard has three times as many cards as Orlando. How many Pokemon cards do they have in all?"""
    jenny_cards = 6
    orlando_cards = jenny_cards + 2
    richard_cards = orlando_cards * 3
    total_cards = jenny_cards + orlando_cards + richard_cards
    result = total_cards
    return result

print(solution())