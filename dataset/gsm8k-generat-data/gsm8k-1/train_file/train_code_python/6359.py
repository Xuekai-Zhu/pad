def solution():
    """Elisa and her two friends went out to dinner. Each of them ordered a meal worth $10. Afterwards, they each had a scoop of the same kind of ice cream. If the $45 Elisa had was enough to pay for everything, what was the cost of a scoop of ice cream?"""
    num_friends = 2
    meal_cost = 10
    total_meal_cost = (num_friends + 1) * meal_cost
    total_cost = 45
    ice_cream_cost = (total_cost - total_meal_cost) / 3
    result = ice_cream_cost
    return result

print(solution())