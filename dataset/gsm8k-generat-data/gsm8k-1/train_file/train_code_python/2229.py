def solution():
    """Alfonso earns $6 each day walking his aunt’s dog. He is saving to buy a mountain bike helmet for $340. Currently, he already has $40. If he walks his aunt's dog 5 days a week, in how many weeks should Alfonso work to buy his mountain bike?"""
    daily_earnings = 6
    helmet_cost = 340
    current_savings = 40
    weekly_savings = daily_earnings * 5
    weeks_to_save = (helmet_cost - current_savings) / weekly_savings
    result = weeks_to_save
    return result

print(solution())