def solution():
    michael_cards = 100
    mark_cards = michael_cards - 10
    lloyd_cards = mark_cards / 3

    total_cards = michael_cards + mark_cards + lloyd_cards

    cards_needed = 300 - total_cards
    result = cards_needed
    return result

print(solution())