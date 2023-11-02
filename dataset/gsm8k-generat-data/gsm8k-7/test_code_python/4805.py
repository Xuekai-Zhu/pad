def solution():
    total_players = 40
    never_lost = total_players / 4

    # Calculate the number of players who have lost to an AI
    lost_to_AI = total_players - never_lost

    result = lost_to_AI
    return result

print(solution())