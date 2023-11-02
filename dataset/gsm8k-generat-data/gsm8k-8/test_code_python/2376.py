def solution():
    # Define the cost of each item
    brownie_cost = 2.5
    ice_cream_cost = 1.0
    syrup_cost = 0.5
    nuts_cost = 1.5

    # Calculate the total cost of Juanita's dessert
    dessert_cost = brownie_cost + (2 * ice_cream_cost) + (2 * syrup_cost) + nuts_cost
    result = dessert_cost
    return result

print(solution())