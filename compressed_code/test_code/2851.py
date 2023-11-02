def solution():
    
    shirt_cost = 3
    saved_amount = 1.5
    remaining_amount = shirt_cost - saved_amount
    weekly_savings = 0.5
    weeks_needed = remaining_amount / weekly_savings
    result = weeks_needed
    return result

print(solution())