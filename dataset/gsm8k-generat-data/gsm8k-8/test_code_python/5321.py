def solution():
    # Calculate the total cost of all the items before discount
    total_cost_before_discount = 20 + 20 + (2*2.5) + 15 + (20*2) + 15

    # Calculate the discount amount
    discount_amount = 0.2 * total_cost_before_discount

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    result = total_cost_after_discount
    return result

print(solution())