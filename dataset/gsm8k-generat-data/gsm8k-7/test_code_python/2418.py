def solution():
    budget = 80
    chicken_cost = 12
    beef_cost_per_pound = 3
    beef_pounds = 5

    # Calculate the total cost of the chicken
    total_chicken_cost = chicken_cost

    # Calculate the total cost of the beef
    total_beef_cost = beef_cost_per_pound * beef_pounds

    # Calculate the total cost of all food items
    total_cost = total_chicken_cost + total_beef_cost

    # Calculate the remaining budget
    remaining_budget = budget - total_cost
    result = remaining_budget
    return result

print(solution())