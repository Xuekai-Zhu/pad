def solution():
    # Calculate the total cost of buying 3 pairs individually
    individual_cost = 10 * 3  # each pair normally costs $10
    # Calculate the cost of buying 3 pairs at once with 10% discount
    discount_cost = (10 * 3) * 0.9  # 10% discount on total cost of 3 pairs
    # Calculate the amount saved by buying 3 pairs at once
    saved_amount = individual_cost - discount_cost
    result = saved_amount
    return result

print(solution())