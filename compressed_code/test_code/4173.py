def solution():
    
    total_cost = 160
    current_saved = 40
    remaining_cost = total_cost - current_saved
    weeks = 8
    amount_per_week = remaining_cost / weeks
    result = amount_per_week
    return result

print(solution())