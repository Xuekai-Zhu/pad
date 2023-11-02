def solution():
    bulls_wins = 70  # The Chicago Bulls won 70 games
    heat_wins = bulls_wins + 5  # The Miami Heat won 5 more games than the Bulls

    # Calculate the total number of games won by the Bulls and the Heat together
    total_wins = bulls_wins + heat_wins
    result = total_wins
    return result

print(solution())