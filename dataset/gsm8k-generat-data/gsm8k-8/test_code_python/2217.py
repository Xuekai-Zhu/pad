def solution():
    # Define the cost of one TV
    tv_cost = 650

    # Calculate the total sales price before discount
    total_price_before_discount = 2 * tv_cost

    # Calculate the discount amount
    discount_amount = 0.25 * total_price_before_discount

    # Calculate the total sales price after discount
    total_price_after_discount = total_price_before_discount - discount_amount

    # Return the amount paid by Mrs. Taylor
    result = total_price_after_discount
    return result

print(solution())