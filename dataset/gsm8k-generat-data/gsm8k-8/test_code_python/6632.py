def solution():
    # Define the number of players on the team and the number of players who received yellow cards
    total_players = 11
    yellow_card_players = total_players - 5

    # Calculate the number of yellow cards given out
    yellow_cards = yellow_card_players

    # Calculate the number of red cards given out (equivalent to 2 yellow cards each)
    red_cards = yellow_cards / 2

    result = red_cards
    return result

print(solution())