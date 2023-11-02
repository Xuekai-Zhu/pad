def solution():
    """Betty is planning to host her friends over for a party. She buys drinks, cakes, and ice creams at a unit cost of $2, $10, and $5 respectively. How much does she spend if she buys 10 drinks, 5 cakes, and 100 ice creams?"""
    drink_cost = 2
    cake_cost = 10
    ice_cream_cost = 5
    num_drinks = 10
    num_cakes = 5
    num_ice_creams = 100
    total_cost = (drink_cost * num_drinks) + (cake_cost * num_cakes) + (ice_cream_cost * num_ice_creams)
    result = total_cost
    return result

print(solution())