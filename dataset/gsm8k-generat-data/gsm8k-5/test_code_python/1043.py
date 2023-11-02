def solution():
    # Calculate the total cost before discount
    total_cost = 2500 + 3500 + 2000  # Cost of the couch, sectional, and everything else combined

    # Calculate the 10% discount
    discount = 0.1 * total_cost

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost - discount

    result = total_cost_after_discount
    return result

print(solution())