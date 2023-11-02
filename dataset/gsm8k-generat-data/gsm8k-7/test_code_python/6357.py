def solution():
    game_cost = 50.0
    sales_tax = 0.1  # 10% sales tax
    allowance_per_week = 10.0
    savings_percentage = 0.5  # save half of allowance
    total_cost = game_cost * (1 + sales_tax)
    savings_per_week = allowance_per_week * savings_percentage
    weeks_to_save = total_cost / savings_per_week
    result = weeks_to_save
    return result

print(solution())