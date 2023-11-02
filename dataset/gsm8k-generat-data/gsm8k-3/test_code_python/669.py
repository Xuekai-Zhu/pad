def solution():
    """Bella has two times as many marbles as frisbees. She also has 20 more frisbees than deck cards. If she buys 2/5 times more of each item, what would be the total number of the items she will have if she currently has 60 marbles?"""
    # Calculate the current number of frisbees Bella has
    marbles = 60
    frisbees = marbles / 2
    deck_cards = frisbees - 20

    # Calculate the new amount of each item after buying 2/5 times more
    new_marbles = marbles + (2/5 * marbles)
    new_frisbees = frisbees + (2/5 * frisbees)
    new_deck_cards = deck_cards + (2/5 * deck_cards)

    # Calculate the total number of items Bella will have
    total_items = new_marbles + new_frisbees + new_deck_cards

    # Display the total number of items
    result = total_items
    return result

print(solution())