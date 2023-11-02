def solution():
    num_roses = 5 * 12
    cost_per_rose = 6
    discount = 0.2  # 20% discount

    # Calculate the total cost before discount
    total_cost_before_discount = num_roses * cost_per_rose

    # Calculate the total cost after discount
    total_cost = total_cost_before_discount * (1 - discount)
    result = total_cost
    return result

print(solution())