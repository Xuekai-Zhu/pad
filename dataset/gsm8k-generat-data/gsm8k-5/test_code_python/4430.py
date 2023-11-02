def solution():
    current_savings = 20  # Barbara currently has $20
    watch_cost = 100  # The watch costs $100
    weekly_allowance = 5  # Barbara receives $5 allowance every week
    
    # Calculate how many more weeks Barbara needs to save for the watch
    remaining_cost = watch_cost - current_savings
    weeks_to_save = remaining_cost / weekly_allowance
    result = weeks_to_save
    return result

print(solution())