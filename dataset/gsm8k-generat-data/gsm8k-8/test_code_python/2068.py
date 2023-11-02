def solution():
    # Calculate the total number of cards Janessa had before giving any to Dexter
    starting_cards = 4 + 13 + 36

    # Subtract the 4 cards Janessa threw away
    good_cards = starting_cards - 4

    # Subtract the 29 cards Janessa gave to Dexter
    remaining_cards = good_cards - 29
    result = remaining_cards
    return result

print(solution())