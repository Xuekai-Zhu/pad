def solution():
    # Calculate the number of meals per week
    meals_per_week = 1 + 3
    # Calculate the cost per week
    cost_per_week = meals_per_week * 4.00 * 5
    # Calculate the total cost for 16 weeks
    total_cost = cost_per_week * 16
    result = total_cost
    return result

print(solution())