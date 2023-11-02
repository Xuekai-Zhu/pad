def solution():
    michael_cards = 100
    mark_cards = michael_cards - 10
    lloyd_cards = mark_cards / 3

    # Calculate the current total number of cards
    current_total = michael_cards + mark_cards + lloyd_cards

    # Calculate how many more cards they need to collect
    cards_needed = 300 - current_total
    result = cards_needed
    return result

print(solution())