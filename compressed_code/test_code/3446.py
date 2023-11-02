def solution():
    
    watch_cost = 100
    current_savings = 20
    weekly_allowance = 5
    weeks_to_save = (watch_cost - current_savings) / weekly_allowance
    result = weeks_to_save
    return result

print(solution())