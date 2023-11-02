def solution():
    # Define the cost of each phone
    cost_per_phone = 800

    # Calculate the total cost before the discount
    total_cost_before_discount = cost_per_phone * 2

    # Calculate the amount of the discount
    discount_amount = total_cost_before_discount * 0.05

    # Calculate the total cost after the discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    result = total_cost_after_discount
    return result

print(solution())