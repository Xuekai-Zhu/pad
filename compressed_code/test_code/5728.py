def solution():
    
    first_five_days_cost = 100 * 5
    remaining_days = 10 - 5
    after_five_days_cost = 60 * remaining_days
    total_cost = first_five_days_cost + after_five_days_cost
    result = total_cost
    return result

print(solution())