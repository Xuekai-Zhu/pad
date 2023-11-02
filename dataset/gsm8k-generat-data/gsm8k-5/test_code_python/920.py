def solution():
    # Define the cost of each item
    cost_drink = 2
    cost_cake = 10
    cost_ice_cream = 5

    # Define the quantity of each item
    quantity_drink = 10
    quantity_cake = 5
    quantity_ice_cream = 100

    # Calculate the total cost of each item
    total_cost_drink = cost_drink * quantity_drink
    total_cost_cake = cost_cake * quantity_cake
    total_cost_ice_cream = cost_ice_cream * quantity_ice_cream

    # Calculate the total cost of the party
    total_cost = total_cost_drink + total_cost_cake + total_cost_ice_cream
    result = total_cost
    return result

print(solution())