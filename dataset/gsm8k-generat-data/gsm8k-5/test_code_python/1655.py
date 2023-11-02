def solution():
    total_budget = 3000  # Abe's budget is $3000 per month

    # Calculate the amount spent on food
    food_budget = total_budget / 3

    # Calculate the amount spent on restaurant supplies
    supplies_budget = total_budget / 4

    # Calculate the amount spent on wages
    wages_budget = total_budget - food_budget - supplies_budget

    result = wages_budget
    return result

print(solution())