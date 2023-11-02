def solution():
    # Calculate the price of one tub of ice cream
    ice_cream_price = 12 - 2

    # Calculate the total cost of two tubs of ice cream
    total_ice_cream_cost = 2 * ice_cream_price

    # Calculate the number of cans of juice you can buy with $2
    juice_can_quantity = 5

    # Calculate the cost of 10 cans of juice
    juice_cost = (10 // juice_can_quantity) * 2

    # Calculate the final cost
    final_cost = total_ice_cream_cost + juice_cost
    result = final_cost
    return result

print(solution())