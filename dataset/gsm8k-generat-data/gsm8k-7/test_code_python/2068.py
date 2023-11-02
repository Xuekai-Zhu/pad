def solution():
    starting_cards = 4 + 13
    ordered_cards = 36
    bad_cards = 4
    given_cards = 29

    # Calculate the total number of cards Janessa had before throwing away the bad ones
    total_cards = starting_cards + ordered_cards

    # Calculate the number of cards Janessa threw away
    thrown_away = bad_cards

    # Calculate the number of cards Janessa kept
    kept_cards = total_cards - given_cards - thrown_away

    result = kept_cards
    return result

print(solution())