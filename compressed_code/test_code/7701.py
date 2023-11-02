def solution():
    
    food_budget = 80
    chicken_cost = 12
    beef_cost = 3
    beef_pounds = 5
    total_spent = chicken_cost + (beef_cost * beef_pounds)
    remaining_budget = food_budget - total_spent
    result = remaining_budget
    return result

print(solution())