def solution():
    """Anton has three times as many cards in his collection as Heike does. Ann has six times as many cards as Heike does. If Ann has 60 cards, how many more cards does Ann have more than Anton?"""
    heike_cards = 10  # assuming Heike has 10 cards
    anton_cards = 3 * heike_cards
    ann_cards = 6 * heike_cards
    diff_cards = ann_cards - anton_cards
    result = diff_cards
    return result

print(solution())