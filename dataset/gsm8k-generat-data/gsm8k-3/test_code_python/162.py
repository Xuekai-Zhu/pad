def solution():
    """Daniel has a collection of 346 video games. 80 of them, Daniel bought for $12 each. Of the rest, 50% were bought for $7. All others had a price of $3 each. How much did Daniel spend on all the games in his collection?"""
    # Define the number of video games and the cost of each type
    total_games = 346
    games_12 = 80
    games_7 = (total_games - games_12) / 2
    games_3 = total_games - games_12 - games_7

    # Calculate the total cost of each type of game
    cost_12 = games_12 * 12
    cost_7 = games_7 * 7
    cost_3 = games_3 * 3

    # Calculate the total cost of all the games
    total_cost = cost_12 + cost_7 + cost_3

    result = total_cost
    return result

print(solution())