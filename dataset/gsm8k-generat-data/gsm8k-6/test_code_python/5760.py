def solution():
    # Calculate the cost of two tubs of ice cream
    ice_cream_cost = 10  # original price of $12 minus $2 discount
    total_ice_cream_cost = ice_cream_cost * 2  # two tubs of ice cream

    # Calculate the cost of 10 cans of juice
    juice_cost = (2/5) * 10  # $2 for 5 cans, so 10 cans cost $4
    total_juice_cost = juice_cost * 10  # 10 cans of juice

    # Calculate the total cost of the purchase
    total_cost = total_ice_cream_cost + total_juice_cost
    result = total_cost
    return result

print(solution())