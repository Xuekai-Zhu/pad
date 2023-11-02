def solution():
    lion_king_cost = 10
    lion_king_earnings = 200
    star_wars_cost = 25
    lion_king_profit = lion_king_earnings - lion_king_cost
    star_wars_profit = lion_king_profit * 2
    star_wars_earnings = star_wars_cost + star_wars_profit
    result = star_wars_earnings
    return result

print(solution())