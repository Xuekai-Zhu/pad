def solution():
    # Define the unit costs
    drinks_cost = 2
    cakes_cost = 10
    ice_cream_cost = 5

    # Define the quantities of each item bought
    drinks_quantity = 10
    cakes_quantity = 5
    ice_cream_quantity = 100

    # Calculate the total cost
    total_cost = (drinks_cost * drinks_quantity) + (cakes_cost * cakes_quantity) + (ice_cream_cost * ice_cream_quantity)
    result = total_cost
    return result

print(solution())