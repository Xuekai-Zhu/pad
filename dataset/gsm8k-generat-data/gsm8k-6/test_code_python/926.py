def solution():
    # Calculate the total cost of towels for the guest bathroom
    cost_guest = 2 * 40.00

    # Calculate the total cost of towels for the master bathroom
    cost_master = 4 * 50.00

    # Calculate the total cost before discount
    total_cost = cost_guest + cost_master

    # Calculate the discount amount
    discount = 0.20 * total_cost

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount
    result = total_cost_after_discount
    return result

print(solution())