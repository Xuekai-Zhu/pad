def solution():
    """Elisa and her two friends went out to dinner. Each of them ordered a meal worth $10. Afterwards, they each had a scoop of the same kind of ice cream. If the $45 Elisa had was enough to pay for everything, what was the cost of a scoop of ice cream?"""
    # Define the cost of each meal
    meal_cost = 10

    # Calculate the total cost of the meals
    total_meal_cost = meal_cost * 3

    # Calculate the amount of money left for the ice cream
    ice_cream_money = 45 - total_meal_cost

    # Calculate the cost of each scoop of ice cream
    ice_cream_cost = ice_cream_money / 3

    result = round(ice_cream_cost, 2)
    return result

print(solution())