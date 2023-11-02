def solution():
    """Oliver has 4 friends that he is inviting to a party at the arcade. Game tokens cost 30 for $1. Each game costs 2 tokens. If he wants all his friends to get to play 60 games each, how much will it cost?"""
    # Define the number of friends and games
    num_friends = 4
    num_games = 60

    # Calculate the total number of game tokens needed
    total_tokens = num_friends * num_games * 2

    # Calculate the cost of the game tokens
    token_cost = total_tokens / 30

    # return the result rounded to 2 decimal places
    result = round(token_cost, 2)
    return result

print(solution())