def solution():
    # Calculate the number of players who have never lost to an AI
    never_lost = 40 / 4

    # Calculate the number of players who have lost to an AI
    lost_to_AI = 40 - never_lost
    result = lost_to_AI
    return result

print(solution())