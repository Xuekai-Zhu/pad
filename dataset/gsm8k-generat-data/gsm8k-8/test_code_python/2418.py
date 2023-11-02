def solution():
    # Calculate the cost of the chicken bucket
    chicken_cost = 12
    
    # Calculate the cost of the beef
    beef_cost = 5 * 3
    
    # Calculate the total cost of the food
    total_cost = chicken_cost + beef_cost
    
    # Calculate the amount left on the budget
    budget_left = 80 - total_cost
    
    result = budget_left
    return result

print(solution())