def solution():
    
    game_cost = 50
    sales_tax = 0.1
    allowance = 10
    saved_per_week = allowance * 0.5
    total_cost = game_cost + game_cost * sales_tax
    weeks_to_save = total_cost / saved_per_week
    result = weeks_to_save
    return result

print(solution())