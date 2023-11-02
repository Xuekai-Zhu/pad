def solution():
    initial_cards = 4  # Janessa has 4 cards
    cards_from_father = 13  # Janessa's father gave her 13 cards
    total_ordered_cards = 36  # Janessa ordered 36 cards
    bad_cards = 4  # Janessa found 4 bad cards and threw them away
    cards_given_away = 29  # Janessa gave Dexter 29 cards

    # Calculate the total number of cards Janessa had
    total_cards = initial_cards + cards_from_father + total_ordered_cards - bad_cards

    # Calculate the number of cards Janessa kept for herself
    cards_kept = total_cards - cards_given_away
    result = cards_kept
    return result

print(solution())