def solution():
    lion_king_profit = 200 - 10  # profit earned by The Lion King
    star_wars_profit = lion_king_profit * 2  # profit earned by Star Wars, which is half of Lion King's profit
    star_wars_cost = 25  # cost to make Star Wars
    star_wars_earnings = star_wars_profit + star_wars_cost  # total earnings of Star Wars
    result = star_wars_earnings / 1000000  # convert the earnings into millions
    return result

print(solution())