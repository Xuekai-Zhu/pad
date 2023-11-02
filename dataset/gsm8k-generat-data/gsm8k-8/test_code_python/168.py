def solution():
    # Calculate the total cost of the order before discount
    total_cost = 2*15 + 6*3 + 6*2
    # Check if the order qualifies for the discount
    if total_cost > 50:
        # Calculate the discount
        discount = 0.1 * total_cost
        # Calculate the total cost after discount
        total_cost_after_discount = total_cost - discount
    else:
        # If the order does not qualify for the discount, the total cost remains the same
        total_cost_after_discount = total_cost
    result = total_cost_after_discount
    return result

print(solution())