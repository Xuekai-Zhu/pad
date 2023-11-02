def solution():
    """Daniel has a collection of 346 video games. 80 of them, Daniel bought for $12 each. Of the rest, 50% were bought for $7. All others had a price of $3 each. How much did Daniel spend on all the games in his collection?"""
    total_games = 346
    expensive_games = 80
    expensive_price = 12
    cheap_price = 3
    half_rest = (total_games - expensive_games) / 2
    half_rest_price = 7
    spent_on_expensive = expensive_games * expensive_price
    spent_on_half_rest = half_rest * half_rest_price
    spent_on_cheaps = (total_games - expensive_games - half_rest) * cheap_price
    total_spent = spent_on_expensive + spent_on_half_rest + spent_on_cheaps
    result = total_spent
    return result

print(solution())