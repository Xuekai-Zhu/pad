def solution():
    cost_of_playstation = 500
    money_from_birthday = 200
    money_from_christmas = 150
    money_to_raise = cost_of_playstation - money_from_birthday - money_from_christmas
    price_per_game = 7.5
    games_to_sell = money_to_raise / price_per_game
    result = games_to_sell
    return result

print(solution())