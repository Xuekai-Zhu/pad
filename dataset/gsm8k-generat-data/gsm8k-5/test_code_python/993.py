def solution():
    cards_to_keep = 15  # Rick decides to keep only 15 cards
    cards_given_away = 130 - cards_to_keep  # Rick gives away the remaining cards
    cards_given_to_friends = 8 * 12  # Rick gives 12 cards each to 8 of his friends
    cards_given_to_sisters = 2 * 3  # Rick gives 3 cards each to his 2 sisters
    cards_given_to_Miguel = cards_given_away - cards_given_to_friends - cards_given_to_sisters
    result = cards_given_to_Miguel
    return result

print(solution())