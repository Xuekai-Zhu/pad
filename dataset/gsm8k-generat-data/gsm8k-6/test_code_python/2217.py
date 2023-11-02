def solution():
    # Calculate the total cost before the discount
    total_cost = 2 * 650  # Mrs. Taylor bought two smart TVs that cost $650 each
    # Calculate the discount amount
    discount = 0.25 * total_cost  # the total sales price had a 25% discount
    # Calculate the cost after the discount
    cost_after_discount = total_cost - discount
    result = cost_after_discount
    return result

print(solution())