def solution():
    
    current_savings = 20
    watch_cost = 100
    weekly_allowance = 5
    weeks_needed = (watch_cost - current_savings) / weekly_allowance
    result = weeks_needed
    return result

print(solution())