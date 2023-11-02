def solution():
    goal_amount = 5000
    current_amount = 2900
    monthly_savings = 700
    months_needed = (goal_amount - current_amount) / monthly_savings
    result = months_needed
    return result

print(solution())