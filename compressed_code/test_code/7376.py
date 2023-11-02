def solution():
    
    num_friends = 4
    num_games = 60
    token_cost = 30
    tokens_per_dollar = 30
    tokens_per_game = 2
    total_tokens_needed = num_friends * num_games * tokens_per_game
    total_cost = total_tokens_needed / tokens_per_dollar
    result = total_cost
    return result

print(solution())