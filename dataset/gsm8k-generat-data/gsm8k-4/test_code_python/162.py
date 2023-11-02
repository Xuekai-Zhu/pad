def solution():
    """Daniel has a collection of 346 video games. 80 of them, Daniel bought for $12 each. Of the rest, 50% were bought for $7. All others had a price of $3 each. How much did Daniel spend on all the games in his collection?"""
    # Define the total number of games and the number of games bought for $12
    total_games = 346
    games_12_dollars = 80

    # Calculate the cost of the games bought for $12 each
    cost_12_dollars = games_12_dollars * 12

    # Calculate the remaining number of games
    remaining_games = total_games - games_12_dollars

    # Calculate the number of games bought for $7 and their cost
    games_7_dollars = remaining_games // 2
    cost_7_dollars = games_7_dollars * 7

    # Calculate the number of games bought for $3 and their cost
    games_3_dollars = remaining_games - games_7_dollars
    cost_3_dollars = games_3_dollars * 3

    # Calculate the total cost of all the games in the collection
    total_cost = cost_12_dollars + cost_7_dollars + cost_3_dollars

    # return the result
    result = total_cost
    return result

print(solution())