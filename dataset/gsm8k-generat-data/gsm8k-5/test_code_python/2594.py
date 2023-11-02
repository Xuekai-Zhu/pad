def solution():
    games_per_month = 3  # John plays paintball 3 times a month
    paintballs_per_game = 3  # John buys 3 boxes of paintballs per game
    cost_per_box = 25  # Each box of paintballs costs $25

    # Calculate the total cost of paintballs per month
    total_cost = games_per_month * paintballs_per_game * cost_per_box
    result = total_cost
    return result

print(solution())