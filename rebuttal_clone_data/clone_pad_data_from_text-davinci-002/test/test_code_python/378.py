def solution():
    marbles = 60
    frisbees = marbles / 2
    deck_cards = frisbees - 20
    new_marbles = marbles + (marbles * 2/5)
    new_frisbees = frisbees + (frisbees * 2/5)
    new_deck_cards = deck_cards + (deck_cards * 2/5)
    result = new_marbles + new_frisbees + new_deck_cards
    return result

print(solution())