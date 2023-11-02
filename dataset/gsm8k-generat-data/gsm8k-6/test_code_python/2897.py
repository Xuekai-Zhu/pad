def solution():
    # Calculate the cost of 12 bottles of sunscreen before the discount
    cost_before_discount = 12 * 30  # each bottle costs $30 and Juanita buys 12 bottles

    # Calculate the cost of 12 bottles of sunscreen after the 30% discount
    cost_after_discount = cost_before_discount * 0.7  # 30% off means Juanita pays 70% of the original cost

    result = cost_after_discount
    return result

print(solution())