def solution():
    total_budget = 240  # Total budget of house rental and food budget is $240
    food_budget_percentage = 60  # Food budget is 60% of house rental budget
    phone_budget_percentage = 10  # Phone bill budget is 10% of food budget

    # Calculate the food budget
    food_budget = (food_budget_percentage / 100) * total_budget

    # Calculate the phone bill budget
    phone_budget = (phone_budget_percentage / 100) * food_budget

    # Calculate the total monthly budget
    total_monthly_budget = food_budget + phone_budget + (total_budget - food_budget)
    result = total_monthly_budget
    return result

print(solution())