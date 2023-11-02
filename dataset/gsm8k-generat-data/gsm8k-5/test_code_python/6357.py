def solution():
    game_cost = 50  # The video game costs $50
    sales_tax_rate = 0.1  # The sales tax rate is 10%
    allowance_per_week = 10  # Nina receives $10 allowance per week
    savings_percentage = 0.5  # Nina plans to save half of her allowance
    total_cost = game_cost * (1 + sales_tax_rate)  # The total cost including sales tax
    amount_saved_per_week = allowance_per_week * savings_percentage  # Nina saves half of her allowance per week

    # Calculate the number of weeks it will take for Nina to save enough money
    weeks_to_save = total_cost / amount_saved_per_week
    result = weeks_to_save
    return result

print(solution())