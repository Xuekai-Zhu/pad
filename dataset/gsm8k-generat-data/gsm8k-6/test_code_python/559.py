def solution():
    # Calculate Luna's food budget and rental budget
    total_budget = 240
    food_budget = 0.6 * total_budget
    rental_budget = total_budget - food_budget
    
    # Calculate Luna's phone bill budget
    phone_budget = 0.1 * food_budget
    
    # Calculate Luna's total monthly budget
    total_monthly_budget = rental_budget + food_budget + phone_budget
    result = total_monthly_budget
    return result

print(solution())