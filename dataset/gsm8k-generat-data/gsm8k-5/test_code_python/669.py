def solution():
    marbles = 60  # Bella currently has 60 marbles
    frisbees = marbles / 2  # Bella has two times as many marbles as frisbees
    deck_cards = frisbees - 20  # Bella has 20 more frisbees than deck cards

    # Calculate 2/5 times more of each item
    marbles_more = marbles * (2/5)
    frisbees_more = frisbees * (2/5)
    deck_cards_more = deck_cards * (2/5)

    # Calculate the total number of each item after buying 2/5 times more
    total_marbles = marbles + marbles_more
    total_frisbees = frisbees + frisbees_more
    total_deck_cards = deck_cards + deck_cards_more
    result = total_marbles + total_frisbees + total_deck_cards
    return result

print(solution())