def solution():
    # Calculate the cost of the first 80 games
    cost_80_games = 80 * 12

    # Calculate the number of games that were not bought for $12
    rest_of_games = 346 - 80

    # Calculate the number of games that were bought for $7
    num_games_7_dollars = 0.5 * rest_of_games

    # Calculate the cost of the games that were bought for $7
    cost_7_dollars_games = num_games_7_dollars * 7

    # Calculate the number of games that were bought for $3
    num_games_3_dollars = rest_of_games - num_games_7_dollars

    # Calculate the cost of the games that were bought for $3
    cost_3_dollars_games = num_games_3_dollars * 3

    # Calculate the total cost of all the games
    total_cost = cost_80_games + cost_7_dollars_games + cost_3_dollars_games
    result = total_cost
    return result

print(solution())