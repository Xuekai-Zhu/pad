def solution():
    lion_king_cost = 10
    lion_king_earnings = 200
    star_wars_cost = 25
    star_wars_profit = 2 * (lion_king_earnings - lion_king_cost) # half of Lion King's profit
    
    # Calculate Star Wars' earnings
    star_wars_earnings = star_wars_cost + star_wars_profit
    
    return star_wars_earnings

The output of the above function will be the number of millions of dollars that Star Wars earned.

print(solution())