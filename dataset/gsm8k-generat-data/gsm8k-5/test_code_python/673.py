def solution():
    cost_per_ball = 0.10  # Cost of each ping pong ball
    quantity = 10000  # Quantity of ping pong balls purchased
    discount = 0.30  # Discount given for bulk purchase

    # Calculate the total cost before discount
    total_cost_before_discount = cost_per_ball * quantity

    # Calculate the amount of discount
    total_discount = total_cost_before_discount * discount

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - total_discount
    result = total_cost_after_discount
    return result

print(solution())