def solution():
    # Calculate the total cost of the meals
    total_meal_cost = 3 * 10  # each person ordered a meal worth $10

    # Calculate the remaining amount after paying for the meals
    remaining_amount = 45 - total_meal_cost

    # Calculate the cost of one scoop of ice cream
    cost_of_scoop = remaining_amount / 3

    result = cost_of_scoop
    return result

print(solution())