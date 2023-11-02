def solution():
    initial_cards = 4
    cards_from_ebay = 36
    cards_given_away = 29
    cards_kept = initial_cards + cards_from_ebay - cards_given_away
    result = cards_kept
    return result

print(solution())