def solution():
    # Let x be the number of cards Heike has
    x = Ann_cards / 6

    # Anton has three times as many cards as Heike, so he has 3x cards
    Anton_cards = 3 * x

    # Ann has 60 cards, so she has 6x cards
    Ann_cards = 60

    # Calculate how many more cards Ann has than Anton
    diff = Ann_cards - Anton_cards
    result = diff
    return result

print(solution())