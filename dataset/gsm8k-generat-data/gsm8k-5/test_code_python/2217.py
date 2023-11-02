def solution():
    cost_of_one_television = 650  # Each television costs $650
    quantity_of_television = 2  # Mrs. Taylor bought 2 televisions
    discount = 0.25  # Mrs. Taylor got a 25% discount

    # Calculate the total cost before the discount
    total_cost_before_discount = cost_of_one_television * quantity_of_television

    # Calculate the amount of discount
    amount_of_discount = total_cost_before_discount * discount

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost_before_discount - amount_of_discount
    result = total_cost_after_discount
    return result

print(solution())