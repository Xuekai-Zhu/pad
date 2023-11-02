def solution():
    num_friends = 4
    num_games_per_friend = 60
    cost_of_tokens = 1/30  # $1 = 30 tokens
    tokens_per_game = 2

    # Calculate the total number of games that Oliver's friends will play
    total_num_games = num_friends * num_games_per_friend

    # Calculate the total cost of all tokens needed for the games
    total_token_cost = total_num_games * tokens_per_game * cost_of_tokens

    result = total_token_cost
    return result

print(solution())