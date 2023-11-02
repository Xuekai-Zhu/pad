def solution():
    """Nicole collected 400 Pokemon cards. Cindy collected twice as many, and Rex collected half of Nicole and Cindy's combined total.
    If Rex divided his card equally among himself and his three younger siblings, how many cards does Rex have left?"""
    nicole_cards = 400
    cindy_cards = nicole_cards * 2
    combined_total = nicole_cards + cindy_cards
    rex_cards = combined_total / 2
    rex_cards_left = rex_cards % 4
    result = rex_cards_left
    return result

print(solution())