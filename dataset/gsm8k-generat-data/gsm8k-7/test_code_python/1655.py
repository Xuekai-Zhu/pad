def solution():
    budget = 3000
    food_cost = budget / 3
    supply_cost = budget / 4

    # Calculate the total cost of food and restaurant supplies
    total_food_and_supplies = food_cost + supply_cost

    # Calculate the cost of employee wages
    wage_cost = budget - total_food_and_supplies
    result = wage_cost
    return result

print(solution())