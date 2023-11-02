def solution():
    """Ice cream costs $2.00 and toppings cost $0.50 per topping. How much does a sundae with 10 toppings cost?"""
    ice_cream_cost = 2
    toppings_cost = 0.5
    num_toppings = 10
    total_cost = ice_cream_cost + (num_toppings * toppings_cost)
    result = total_cost
    return result

print(solution())