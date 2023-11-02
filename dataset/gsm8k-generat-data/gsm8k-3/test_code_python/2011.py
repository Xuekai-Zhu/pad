def solution():
    """Oliver has 4 friends that he is inviting to a party at the arcade. Game tokens cost 30 for $1. Each game costs 2 tokens. If he wants all his friends to get to play 60 games each, how much will it cost?"""
    # Define the number of friends and games each friend will play
    num_friends = 4
    num_games = 60

    # Define the tokens needed per game
    tokens_per_game = 2

    # Define the cost of tokens
    token_cost = 30 # cents per token, or $0.30 per token

    # Calculate the total tokens needed
    total_tokens = num_friends * num_games * tokens_per_game

    # Calculate the total cost in dollars
    total_cost = total_tokens / 100 * token_cost

    # Return the total cost rounded to 2 decimal places
    result = round(total_cost, 2)
    return result

print(solution())