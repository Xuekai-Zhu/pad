def solution():
    
    daily_earnings = 6
    helmet_cost = 340
    current_savings = 40
    weekly_savings = daily_earnings * 5
    weeks_to_save = (helmet_cost - current_savings) / weekly_savings
    result = weeks_to_save
    return result

print(solution())