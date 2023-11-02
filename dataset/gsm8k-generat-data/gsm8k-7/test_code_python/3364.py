def solution():
    regular_price = 50
    discount = 0.4  # 40% off
    num_shirts = 2

    # Calculate the total cost of the shirts before the discount
    total_cost_before_discount = regular_price * num_shirts

    # Calculate the amount of the discount
    total_discount = total_cost_before_discount * discount

    # Calculate the total cost of the shirts after the discount
    total_cost_after_discount = total_cost_before_discount - total_discount
    result = total_cost_after_discount
    return result

print(solution())