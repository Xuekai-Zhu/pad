def solution():
    """Elisa and her two friends went out to dinner. Each of them ordered a meal worth $10. Afterwards, they each had a scoop of the same kind of ice cream. If the $45 Elisa had was enough to pay for everything, what was the cost of a scoop of ice cream?"""
    # Define the cost of one meal
    MEAL_PRICE = 10

    # Define the total cost of the meals
    total_meal_cost = 3 * MEAL_PRICE

    # Calculate the cost of the ice cream
    ice_cream_cost = 45 - total_meal_cost
    cost_per_scoop = ice_cream_cost / 3

    # Display the cost per scoop
    result = cost_per_scoop
    return result

print(solution())