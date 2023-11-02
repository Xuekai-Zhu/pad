def solution():
    # Find the number of cards Karen took out
    cards_removed = (1/6) * 48

    # Find the number of cards originally in the box
    original_cards = 83 - cards_removed

    result = original_cards
    return result

print(solution())