def solution():
    
    total_goal = 5000
    current_savings = 2900
    monthly_savings = 700
    remaining_goal = total_goal - current_savings
    months_needed = remaining_goal / monthly_savings
    result = months_needed
    return result

print(solution())