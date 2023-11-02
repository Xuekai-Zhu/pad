def solution():
    # Calculate the cost of the guest bathroom towel sets
    guest_bathroom_cost = 2 * 40.0  # 2 sets of towels at $40 each

    # Calculate the cost of the master bathroom towel sets
    master_bathroom_cost = 4 * 50.0  # 4 sets of towels at $50 each

    # Calculate the total cost before the discount
    total_cost = guest_bathroom_cost + master_bathroom_cost

    # Calculate the amount of the discount
    discount_amount = total_cost * 0.2

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost - discount_amount
    result = total_cost_after_discount
    return result

print(solution())