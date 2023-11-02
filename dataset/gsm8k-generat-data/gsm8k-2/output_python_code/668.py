def solution():
    """Bella has two times as many marbles as frisbees. She also has 20 more frisbees than deck cards. If she buys 2/5 times more of each item, what would be the total number of the items she will have if she currently has 60 marbles?"""
    current_marbles = 60
    frisbees = (current_marbles / 2) + 20
    deck_cards = frisbees - 20
    marble_increase = current_marbles * (2 / 5)
    frisbee_increase = frisbees * (2 / 5)
    deck_card_increase = deck_cards * (2 / 5)
    total_marbles = current_marbles + marble_increase
    total_frisbees = frisbees + frisbee_increase
    total_deck_cards = deck_cards + deck_card_increase
    result = total_marbles + total_frisbees + total_deck_cards
    return result

print(solution())