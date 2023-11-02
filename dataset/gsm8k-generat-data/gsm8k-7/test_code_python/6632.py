def solution():
    total_players = 11
    non_cautious_players = 5
    cautioned_players = total_players - non_cautious_players

    # Calculate the number of yellow cards received by the cautioned players
    num_yellow_cards = cautioned_players * 1

    # Calculate the number of red cards that the whole team would collect
    num_red_cards = num_yellow_cards / 2
    result = num_red_cards
    return result

print(solution())