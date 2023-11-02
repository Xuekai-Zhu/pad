def solution()
    game_cost = 50
    sales_tax = 10
    weekly_allowance = 10
    weekly_savings = weekly_allowance / 2
    weeks_needed = game_cost / weekly_savings
    result = weeks_needed
    return result

print(solution())