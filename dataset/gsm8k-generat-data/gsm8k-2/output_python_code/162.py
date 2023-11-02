def solution():
    """Daniel has a collection of 346 video games. 80 of them, Daniel bought for $12 each. Of the rest, 50% were bought for $7. All others had a price of $3 each. How much did Daniel spend on all the games in his collection?"""
    num_expensive_games = 80
    expensive_game_price = 12
    half_num_cheap_games = (346 - num_expensive_games) / 2
    cheap_game_price = 3
    half_cheap_games_price = half_num_cheap_games * cheap_game_price
    half_expensive_games_price = (num_expensive_games - half_num_cheap_games) * expensive_game_price
    remaining_games_price = (346 - num_expensive_games - half_num_cheap_games) * 7
    total_price = half_cheap_games_price + half_expensive_games_price + remaining_games_price
    result = total_price
    return result

print(solution())