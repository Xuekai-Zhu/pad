def solution():
    # Calculate the cost of all the items before the discount
    total_cost_before_discount = 20 + 20 + (2 * 2.5) + 15 + (2 * 20) + 15

    # Calculate the discount amount
    discount_amount = total_cost_before_discount * 0.2

    # Calculate the total cost with the discount
    total_cost_with_discount = total_cost_before_discount - discount_amount

    result = total_cost_with_discount + 20  # Add the cost of adopting the puppy
    return result

print(solution())