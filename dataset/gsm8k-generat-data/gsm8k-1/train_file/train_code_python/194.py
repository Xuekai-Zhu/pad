def solution():
    """Mary bought 5 boxes of drinks at $6 each box and 10 boxes of pizzas at $14 each box for her pizza party. She paid $200 for all the items. How much change did she get back?"""
    drinks_cost = 5 * 6
    pizzas_cost = 10 * 14
    total_cost = drinks_cost + pizzas_cost
    payment = 200
    change = payment - total_cost
    result = change
    return result

print(solution())