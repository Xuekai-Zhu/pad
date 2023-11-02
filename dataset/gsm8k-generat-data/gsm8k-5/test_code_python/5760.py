def solution():
    # Calculate the cost of one tub of ice cream after the discount
    ice_cream_cost = 12 - 2  # original price of $12 minus $2 discount
    # Calculate the cost of one can of juice
    juice_cost = 2/5  # $2 for 5 cans, so one can costs $2/5
    # Calculate the total cost of two tubs of ice cream
    ice_cream_total = 2 * ice_cream_cost
    # Calculate the total cost of 10 cans of juice
    juice_total = 10 * juice_cost
    # Calculate the overall cost
    overall_cost = ice_cream_total + juice_total
    result = overall_cost
    return result

print(solution())