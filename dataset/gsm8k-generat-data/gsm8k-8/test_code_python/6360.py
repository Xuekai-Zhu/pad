def solution():
    # Define the cost of one meal
    meal_cost = 10

    # Calculate the total cost of meals
    total_meal_cost = 3 * meal_cost

    # Calculate the remaining amount after paying for meals
    remaining_amount = 45 - total_meal_cost

    # Calculate the cost of one scoop of ice cream
    ice_cream_cost = remaining_amount / 3
    result = ice_cream_cost
    return result

print(solution())