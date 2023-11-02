def solution():
    """Betty is planning to host her friends over for a party. She buys drinks, cakes, and ice creams at a unit cost of $2, $10, and $5 respectively. How much does she spend if she buys 10 drinks, 5 cakes, and 100 ice creams?"""
    cost_of_drink = 2
    cost_of_cake = 10
    cost_of_ice_cream = 5
    units_of_drink = 10
    units_of_cake = 5
    units_of_ice_cream = 100
    total_cost = (cost_of_drink*units_of_drink) + (cost_of_cake*units_of_cake) + (cost_of_ice_cream*units_of_ice_cream)
    result = total_cost
    return result

print(solution())