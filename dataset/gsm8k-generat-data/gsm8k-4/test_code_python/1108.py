def solution():
    """Anton has three times as many cards in his collection as Heike does. Ann has six times as many cards as Heike does. If Ann has 60 cards, how many more cards does Ann have more than Anton?"""
    # Determine how many cards Heike has
    heike_cards = 60 / 6

    # Determine how many cards Anton has
    anton_cards = heike_cards / 3

    # Determine how many more cards Ann has than Anton
    ann_cards_more_than_anton = 60 - anton_cards

    result = ann_cards_more_than_anton
    return result

print(solution())