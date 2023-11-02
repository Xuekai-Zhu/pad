def solution():
    num_friends = 4  # Oliver has 4 friends
    num_games_each = 60  # Oliver wants each friend to play 60 games
    tokens_per_game = 2  # Each game costs 2 tokens
    tokens_per_dollar = 30  # Tokens cost 30 for $1

    # Calculate the total number of tokens needed for all the games
    total_tokens = num_friends * num_games_each * tokens_per_game

    # Calculate the total cost in dollars
    total_cost = total_tokens / tokens_per_dollar
    result = total_cost
    return result

print(solution())