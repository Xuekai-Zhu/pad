def solution():
    
    marbles = 60
    frisbees = marbles / 2
    deck_cards = frisbees - 20
    total_items = (marbles + (2/5 * marbles)) + (frisbees + (2/5 * frisbees)) + (deck_cards + (2/5 * deck_cards))
    result = total_items
    return result

print(solution())