def solution():
    num_shirts = 2
    shirt_price = 30
    discount = 0.4  # 40% discount

    # Calculate the total cost before discount
    total_cost_before_discount = num_shirts * shirt_price

    # Calculate the discount amount
    discount_amount = total_cost_before_discount * discount

    # Calculate the total cost after discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    result = total_cost_after_discount
    return result

print(solution())