def solution():
    # Calculate the total amount spent by Daniel on the 80 games bought for $12 each
    amount_spent_on_12_dollar_games = 80 * 12

    # Calculate the number of games that Daniel did not buy for $12
    remaining_games = 346 - 80

    # Calculate the number of games bought for $7
    games_bought_for_7_dollars = remaining_games * 0.5

    # Calculate the total amount spent on these games
    amount_spent_on_7_dollar_games = games_bought_for_7_dollars * 7

    # Calculate the number of games bought for $3
    games_bought_for_3_dollars = remaining_games - games_bought_for_7_dollars

    # Calculate the total amount spent on these games
    amount_spent_on_3_dollar_games = games_bought_for_3_dollars * 3

    # Calculate the total amount spent by Daniel on all games
    total_amount_spent = amount_spent_on_12_dollar_games + amount_spent_on_7_dollar_games + amount_spent_on_3_dollar_games

    result = total_amount_spent

    return result

print(solution())