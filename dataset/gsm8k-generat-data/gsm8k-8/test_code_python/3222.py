def solution():
    nicole_cards = 400
    cindy_cards = 2 * nicole_cards
    total_cards = nicole_cards + cindy_cards
    rex_cards = total_cards / 2
    rex_cards_per_child = rex_cards / 4

    # Calculate how many cards Rex has left
    rex_cards_left = rex_cards % 4
    result = rex_cards_left
    return result

print(solution())