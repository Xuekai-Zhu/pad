def solution():
    """Oliver has 4 friends that he is inviting to a party at the arcade. Game tokens cost 30 for $1. Each game costs 2 tokens. If he wants all his friends to get to play 60 games each, how much will it cost?"""
    friends = 4
    games_per_friend = 60
    tokens_per_dollar = 30
    tokens_per_game = 2
    total_games = friends * games_per_friend
    total_tokens = total_games * tokens_per_game
    total_cost = total_tokens / tokens_per_dollar
    result = total_cost
    return result

print(solution())