def solution():
    # Calculate the cost of the 80 video games that were bought for $12 each
    cost_of_80_games = 80 * 12

    # Calculate the number of video games that were not bought for $12 each
    num_other_games = 346 - 80

    # Calculate the number of video games that were bought for $7 each
    num_7dollar_games = int(num_other_games / 2)
    cost_of_7dollar_games = num_7dollar_games * 7

    # Calculate the number of video games that were bought for $3 each
    num_3dollar_games = num_other_games - num_7dollar_games
    cost_of_3dollar_games = num_3dollar_games * 3

    # Calculate the total cost of all the video games in Daniel's collection
    total_cost = cost_of_80_games + cost_of_7dollar_games + cost_of_3dollar_games
    result = total_cost
    return result

print(solution())