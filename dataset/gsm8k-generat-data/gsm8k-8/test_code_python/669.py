def solution():
    # Define the current number of marbles
    current_marbles = 60

    # Calculate the current number of frisbees and deck cards
    current_frisbees = (current_marbles / 2) + 20
    current_deck_cards = (current_frisbees - 20) / 2

    # Calculate the new number of items
    new_marbles = current_marbles * 1.4
    new_frisbees = current_frisbees * 1.4
    new_deck_cards = current_deck_cards * 1.4

    # Calculate the total number of items
    total_items = new_marbles + new_frisbees + new_deck_cards
    result = total_items
    return result

print(solution())