def solution():
    """Oliver has 4 friends that he is inviting to a party at the arcade. Game tokens cost 30 for $1. Each game costs 2 tokens. If he wants all his friends to get to play 60 games each, how much will it cost?"""
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