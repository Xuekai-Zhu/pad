def solution():
    # Calculate the cost of the sets for the guest bathroom
    guest_cost = 2 * 40

    # Calculate the cost of the sets for the master bathroom
    master_cost = 4 * 50

    # Calculate the total cost before the discount
    total_cost = guest_cost + master_cost

    # Calculate the amount of the discount
    discount = 0.2 * total_cost

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost - discount
    result = total_cost_after_discount
    return result

print(solution())