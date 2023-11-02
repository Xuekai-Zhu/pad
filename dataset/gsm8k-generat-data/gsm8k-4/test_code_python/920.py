def solution():
    """Betty is planning to host her friends over for a party. She buys drinks, cakes, and ice creams at a unit cost of $2, $10, and $5 respectively. How much does she spend if she buys 10 drinks, 5 cakes, and 100 ice creams?"""
    # Define the unit costs of drinks, cakes, and ice creams
    DRINK_COST = 2
    CAKE_COST = 10
    ICE_CREAM_COST = 5

    # Define the quantities of drinks, cakes, and ice creams
    drinks_quantity = 10
    cakes_quantity = 5
    ice_cream_quantity = 100

    # Calculate the total cost of drinks
    drinks_cost = DRINK_COST * drinks_quantity

    # Calculate the total cost of cakes
    cakes_cost = CAKE_COST * cakes_quantity

    # Calculate the total cost of ice creams
    ice_cream_cost = ICE_CREAM_COST * ice_cream_quantity

    # Calculate the total cost of all items
    total_cost = drinks_cost + cakes_cost + ice_cream_cost

    # return the result
    result = total_cost
    return result

print(solution())