def solution():
    # Calculate the total cost before the discount
    cost_before_discount = 5 * 3  # John buys 5 toys that each cost $3

    # Calculate the amount of the discount
    discount = 0.2 * cost_before_discount  # John gets a 20% discount

    # Calculate the total cost after the discount
    cost_after_discount = cost_before_discount - discount

    result = cost_after_discount
    return result

print(solution())