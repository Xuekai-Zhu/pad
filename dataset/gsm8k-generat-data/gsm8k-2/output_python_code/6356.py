def solution():
    """Nina wants to buy a new video game with her allowance money. The game cost 50 dollars. Nina also has learned that there is a 10 percent sales tax. She receives 10 dollars a week as an allowance, and thinks she can save half of that. How many weeks will it take for Nina to be able to buy the new video game with her savings?"""
    game_cost = 50
    sales_tax = 0.1
    allowance = 10
    saved_per_week = allowance * 0.5
    total_cost = game_cost + game_cost * sales_tax
    weeks_to_save = total_cost / saved_per_week
    result = weeks_to_save
    return result

print(solution())