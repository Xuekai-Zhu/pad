def solution():
    """Bella has two times as many marbles as frisbees. She also has 20 more frisbees than deck cards. If she buys 2/5 times more of each item, what would be the total number of the items she will have if she currently has 60 marbles?"""
    marbles = 60
    frisbees = marbles / 2
    deck_cards = frisbees - 20
    total_items = (marbles + (2/5 * marbles)) + (frisbees + (2/5 * frisbees)) + (deck_cards + (2/5 * deck_cards))
    result = total_items
    return result

print(solution())