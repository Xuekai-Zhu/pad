def solution():
    # Find Cindy's number of Pokemon cards
    cindy_cards = 2 * 400

    # Find Nicole and Cindy's combined number of Pokemon cards
    nicole_cindy_total = 400 + cindy_cards

    # Find Rex's number of Pokemon cards
    rex_cards = (1/2) * nicole_cindy_total

    # Find the total number of cards that Rex has after dividing equally among himself and his three younger siblings
    rex_total_cards = rex_cards / 4

    # Find the number of cards that Rex has left
    rex_left_cards = rex_total_cards - rex_cards

    result = rex_left_cards
    return result

print(solution())