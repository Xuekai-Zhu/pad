def solution():
    cards_added = 48
    cards_taken_out = cards_added / 6
    cards_remaining = 83

    # Calculate the total number of cards originally in the box
    original_cards = cards_remaining - cards_taken_out
    result = original_cards
    return result

print(solution())