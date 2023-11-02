def solution():
    current_savings = 20
    watch_cost = 100
    weekly_allowance = 5
    
    # Calculate the amount of money Barbara still needs to save
    amount_left_to_save = watch_cost - current_savings
    
    # Calculate how many weeks it will take to save the rest of the money
    weeks_to_save = amount_left_to_save / weekly_allowance
    
    result = weeks_to_save
    return result

print(solution())