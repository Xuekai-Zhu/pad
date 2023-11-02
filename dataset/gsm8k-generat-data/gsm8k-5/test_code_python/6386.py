def solution():
    air_hockey_games = 2  # Nathan played 2 times air hockey
    basketball_games = 4  # Nathan played 4 times basketball
    cost_per_game = 3  # Each game costs 3 tokens

    # Calculate the total number of tokens Nathan used
    total_tokens = (air_hockey_games + basketball_games) * cost_per_game
    result = total_tokens
    return result

print(solution())