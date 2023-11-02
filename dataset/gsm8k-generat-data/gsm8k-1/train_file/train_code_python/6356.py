def solution():
    """Nina wants to buy a new video game with her allowance money. The game cost 50 dollars. Nina also has learned that there is a 10 percent sales tax. She receives 10 dollars a week as an allowance, and thinks she can save half of that. How many weeks will it take for Nina to be able to buy the new video game with her savings?"""
    game_cost = 50
    sales_tax_percent = 10
    sales_tax = game_cost * (sales_tax_percent / 100)
    total_cost = game_cost + sales_tax
    savings_per_week = 5
    weeks_to_save = total_cost / savings_per_week
    result = weeks_to_save
    return result

print(solution())