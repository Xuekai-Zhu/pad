def solution():
    allowance_per_week = 5
    total_cost = 100
    current_savings = 20
    needed_savings = total_cost - current_savings
    weeks_needed = needed_savings / allowance_per_week
    result = weeks_needed
    return result

print(solution())