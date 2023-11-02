def solution():
    roses = 5 * 12   # Jan buys 5 dozen roses
    cost_per_rose = 6   # Each rose costs $6
    discount = 0.8  # Jan only needs to pay 80% of the total cost

    # Calculate the total cost of the roses before the discount
    total_cost_before_discount = roses * cost_per_rose

    # Calculate the cost after the discount
    total_cost_after_discount = total_cost_before_discount * discount
    result = total_cost_after_discount
    return result

print(solution())