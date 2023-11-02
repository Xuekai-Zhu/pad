def solution():
    lion_king_cost = 10
    lion_king_revenue = 200
    star_wars_cost = 25

    # Calculate the profit earned by The Lion King
    lion_king_profit = lion_king_revenue - lion_king_cost

    # Calculate the profit earned by Star Wars
    star_wars_profit = lion_king_profit * 2  # Half of what The Lion King made

    # Calculate the revenue earned by Star Wars
    star_wars_revenue = star_wars_profit + star_wars_cost

    result = star_wars_revenue
    return result

print(solution())