def solution():
    original_ice_cream_price = 12
    ice_cream_discount = 2
    ice_cream_price = original_ice_cream_price - ice_cream_discount

    juice_price = 2/5  # $2 for 5 cans

    num_ice_cream_tubs = 2
    num_juice_cans = 10

    # Calculate the total cost of ice cream
    ice_cream_cost = num_ice_cream_tubs * ice_cream_price

    # Calculate the total cost of juice
    juice_cost = num_juice_cans * juice_price

    # Calculate the total cost of the purchase
    total_cost = ice_cream_cost + juice_cost
    result = total_cost
    return result

print(solution())