def solution():
    
    total_cost = 160
    initial_savings = 40
    weeks_in_two_months = 8
    remaining_cost = total_cost - initial_savings
    savings_per_week = remaining_cost / weeks_in_two_months
    result = savings_per_week
    return result

print(solution())