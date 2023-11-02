def solution():
    """Anton has three times as many cards in his collection as Heike does. Ann has six times as many cards as Heike does. If Ann has 60 cards, how many more cards does Ann have more than Anton?"""
    ann_cards = 60
    heike_cards = ann_cards / 6
    anton_cards = heike_cards / 3
    cards_diff = ann_cards - anton_cards
    result = cards_diff
    return result

print(solution())