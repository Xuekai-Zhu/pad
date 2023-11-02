def solution():
    """Betty is planning to host her friends over for a party. She buys drinks, cakes, and ice creams at a unit cost of $2, $10, and $5 respectively. How much does she spend if she buys 10 drinks, 5 cakes, and 100 ice creams?"""
    # Define the unit cost of drinks, cakes, and ice creams
    DRINK_COST = 2
    CAKE_COST = 10
    ICE_CREAM_COST = 5

    # Define the number of drinks, cakes, and ice creams to be bought
    num_drinks = 10
    num_cakes = 5
    num_ice_creams = 100

    # Calculate the total cost of drinks
    drinks_cost = num_drinks * DRINK_COST

    # Calculate the total cost of cakes
    cake_cost = num_cakes * CAKE_COST

    # Calculate the total cost of ice creams
    ice_cream_cost = num_ice_creams * ICE_CREAM_COST

    # Calculate the total cost of all the items
    total_cost = drinks_cost + cake_cost + ice_cream_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())