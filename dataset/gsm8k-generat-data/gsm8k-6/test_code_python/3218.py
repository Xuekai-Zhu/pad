def solution():
    # Calculate the total number of games played by Ken, Dave, and Jerry
    # Let x be the number of games won by Dave
    x = 7 + 3  # Dave won 3 more games than Jerry
    # Ken won 5 more games than Dave
    y = x + 5
    total_games = x + y + 7  # Jerry won 7 games
    
    result = total_games
    return result

print(solution())