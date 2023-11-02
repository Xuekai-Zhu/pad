def solution():
    nicole_cards = 400
    cindy_cards = nicole_cards * 2
    combined_total = nicole_cards + cindy_cards
    rex_cards = combined_total / 2
    rex_cards_left = rex_cards % 4
    result = rex_cards_left
    return result

print(solution())