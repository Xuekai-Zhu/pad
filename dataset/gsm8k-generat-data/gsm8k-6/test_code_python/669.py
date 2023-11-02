def solution():
    # Determine current number of frisbees
    current_marbles = 60
    current_frisbees = current_marbles / 2

    # Determine current number of deck cards
    current_deck_cards = current_frisbees - 20

    # Calculate the 2/5 more of each item
    more_marbles = (2/5) * current_marbles
    more_frisbees = (2/5) * current_frisbees
    more_deck_cards = (2/5) * current_deck_cards

    # Calculate the total number of items
    total_marbles = current_marbles + more_marbles
    total_frisbees = current_frisbees + more_frisbees
    total_deck_cards = current_deck_cards + more_deck_cards
    total_items = total_marbles + total_frisbees + total_deck_cards

    result = total_items
    return result

print(solution())