def solution():
    total_cards = 365
    brother_sets = 8
    sister_sets = 5
    friend_sets = 2
    cards_per_set = 13

    # Calculate the total number of sets given away
    total_sets = brother_sets + sister_sets + friend_sets

    # Calculate the total number of cards given away
    total_cards_given_away = total_sets * cards_per_set
    result = total_cards_given_away
    return result

print(solution())