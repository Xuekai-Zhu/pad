def solution():
    # Calculate how much Abe spends on food and restaurant supplies
    food_cost = 3000 / 3
    supplies_cost = 3000 / 4
    total_cost = food_cost + supplies_cost

    # Calculate how much Abe spends on wages
    wage_cost = 3000 - total_cost
    result = wage_cost
    return result

print(solution())