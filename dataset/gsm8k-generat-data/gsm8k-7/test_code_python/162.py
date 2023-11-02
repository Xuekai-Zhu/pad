def solution():
    total_games = 346
    price_first_80 = 12
    num_first_80 = 80
    percent_rest_7 = 0.5
    price_rest_7 = 7
    price_rest_3 = 3

    # Calculate the cost of the first 80 games
    cost_first_80 = price_first_80 * num_first_80

    # Calculate the number of games that were not in the first 80
    num_rest = total_games - num_first_80

    # Calculate the number of games bought for $7
    num_rest_7 = num_rest * percent_rest_7

    # Calculate the number of games bought for $3
    num_rest_3 = num_rest - num_rest_7

    # Calculate the total cost of all games
    total_cost = cost_first_80 + (num_rest_7 * price_rest_7) + (num_rest_3 * price_rest_3)
    result = total_cost
    return result

print(solution())