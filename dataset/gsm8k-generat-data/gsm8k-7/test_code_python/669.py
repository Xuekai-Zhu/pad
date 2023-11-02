def solution():
    num_marbles = 60

    # Calculate the number of frisbees Bella has
    num_frisbees = num_marbles / 2

    # Calculate the number of deck cards Bella has
    num_deck_cards = num_frisbees - 20

    # Calculate the 2/5 increase for each item
    increase_factor = 2/5
    marble_increase = num_marbles * increase_factor
    frisbee_increase = num_frisbees * increase_factor
    deck_card_increase = num_deck_cards * increase_factor

    # Calculate the new total number of items
    total_marbles = num_marbles + marble_increase
    total_frisbees = num_frisbees + frisbee_increase
    total_deck_cards = num_deck_cards + deck_card_increase
    total_items = total_marbles + total_frisbees + total_deck_cards
    result = total_items
    return result

print(solution())