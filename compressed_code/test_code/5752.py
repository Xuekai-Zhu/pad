def solution():
    
    console_price = 282
    current_savings = 42
    weekly_allowance = 24
    weeks_needed = (console_price - current_savings) / weekly_allowance
    result = weeks_needed
    return result

print(solution())