def solution():
    # Define the number of friends and games per friend
    num_friends = 4
    games_per_friend = 60

    # Calculate the total number of games to be played
    total_games = num_friends * games_per_friend

    # Calculate the total number of tokens needed for all the games
    total_tokens = total_games * 2

    # Calculate the cost in dollars
    cost_in_dollars = total_tokens / 30

    result = cost_in_dollars
    return result

print(solution())