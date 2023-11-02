def solution():
    # Define Abe's budget
    total_budget = 3000

    # Calculate how much he spends on food
    food_budget = total_budget / 3

    # Calculate how much he spends on restaurant supplies
    supplies_budget = total_budget / 4

    # Calculate how much he spends on wages
    wages_budget = total_budget - food_budget - supplies_budget
    result = wages_budget
    return result

print(solution())