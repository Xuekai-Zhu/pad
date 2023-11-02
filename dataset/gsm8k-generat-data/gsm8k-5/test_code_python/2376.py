def solution():
    brownie_price = 2.5  # The brownie costs $2.50
    ice_cream_price = 1  # Each scoop of ice cream costs $1.00
    syrup_price = 0.5  # Any syrup costs $0.50
    nuts_price = 1.5  # Nuts cost $1.50

    # Calculate the total cost of Juanita's dessert
    dessert_cost = brownie_price + (2 * ice_cream_price) + (2 * syrup_price) + nuts_price
    result = dessert_cost
    return result

print(solution())