def solution():
    # Calculate the number of individuals who like football and play it
    like_play_football = (24/60) * 0.5

    # Calculate the total number of individuals who play football out of a group of 250
    total_football_players = like_play_football * 250

    result = total_football_players
    return result

print(solution())