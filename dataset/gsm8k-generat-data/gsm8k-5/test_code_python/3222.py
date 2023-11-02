def solution():
    nicole_cards = 400
    cindy_cards = 2 * nicole_cards
    combined_cards = nicole_cards + cindy_cards
    rex_cards = combined_cards / 2
    rex_cards_per_person = rex_cards / 4
    rex_leftover_cards = rex_cards % 4

    return rex_leftover_cards

print(solution())