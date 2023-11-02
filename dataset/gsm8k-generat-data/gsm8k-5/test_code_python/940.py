def solution():
    michael_cards = 100  # Michael currently has 100 cards
    mark_cards = 3 * (michael_cards - 10)  # Mark has thrice as many cards as Lloyd but 10 fewer than Michael
    lloyd_cards = (300 - michael_cards - mark_cards)  # Lloyd has the remaining cards they need to collect

    # Calculate the number of cards they need to collect
    cards_to_collect = lloyd_cards - mark_cards
    result = cards_to_collect
    return result

print(solution())