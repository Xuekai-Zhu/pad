def solution():
    # Calculate the total number of games the Giants need to win to make the playoffs
    total_games_needed = ((2/3)*(20+10)) - 12 # they need to win 2/3 of their games over the whole season (30 games)
    result = total_games_needed
    return result

print(solution())