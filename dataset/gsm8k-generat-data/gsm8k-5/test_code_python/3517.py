def solution():
    cost_per_bag = 25  # The bulk bag of mixed nuts costs $25.00
    amount_per_bag = 40  # The bulk bag of mixed nuts holds 40 oz of mixed nuts
    coupon_amount = 5  # There is a $5 coupon available
    total_cost = cost_per_bag - coupon_amount  # Apply the coupon to the total cost
    cost_per_oz = total_cost / amount_per_bag  # Calculate the cost per ounce of mixed nuts
    cost_per_serving = cost_per_oz * 1  # Each serving is 1 oz of mixed nuts
    cost_per_serving_cents = cost_per_serving * 100  # Convert the cost to cents
    result = cost_per_serving_cents
    return result

print(solution())