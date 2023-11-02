def solution():
    num_toys = 5
    toy_price = 3.0
    discount = 0.2  # 20% discount

    # Calculate the total cost of all toys before discount
    total_cost_before_discount = num_toys * toy_price

    # Calculate the discount amount
    discount_amount = total_cost_before_discount * discount

    # Calculate the total cost of all toys after discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    result = total_cost_after_discount
    return result

print(solution())