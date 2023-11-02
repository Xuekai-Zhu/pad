def solution():
    toy_price = 12  # Each toy costs $12.00

    # Calculate the total cost of the toys before the discount
    total_cost_before_discount = 4 * toy_price

    # Calculate the discount amount
    discount_amount = (2 * toy_price) / 2  # Buy one get one half off, so the second toy is half price

    # Calculate the total cost of the toys after the discount
    total_cost_after_discount = total_cost_before_discount - discount_amount

    result = total_cost_after_discount
    return result

print(solution())