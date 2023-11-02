def solution():
    bed_frame_price = 75
    bed_price = bed_frame_price * 10
    discount = 0.2  # 20% off

    # Calculate the total cost of everything before the discount
    total_cost_before_discount = bed_frame_price + bed_price

    # Calculate the amount of the discount
    discount_amount = total_cost_before_discount * discount

    # Calculate the total cost of everything after the discount
    total_cost_after_discount = total_cost_before_discount - discount_amount
    result = total_cost_after_discount
    return result

print(solution())