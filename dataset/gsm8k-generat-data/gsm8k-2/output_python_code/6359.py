def solution():
    """Elisa and her two friends went out to dinner. Each of them ordered a meal worth $10. Afterwards, they each had a scoop of the same kind of ice cream. If the $45 Elisa had was enough to pay for everything, what was the cost of a scoop of ice cream?"""
    total_meal_cost = 3 * 10
    remaining_amount = 45 - total_meal_cost
    cost_of_ice_cream = remaining_amount / 3
    result = cost_of_ice_cream
    return result

print(solution())