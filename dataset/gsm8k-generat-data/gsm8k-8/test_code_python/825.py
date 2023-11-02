def solution():
    # Define the price of the bed frame and calculate the price of the bed
    bed_frame_price = 75
    bed_price = 10 * bed_frame_price

    # Calculate the total price before the discount
    total_price_before_discount = bed_frame_price + bed_price

    # Calculate the amount of the discount
    discount = 0.2 * total_price_before_discount

    # Calculate the total price after the discount
    total_price_after_discount = total_price_before_discount - discount
    result = total_price_after_discount
    return result

print(solution())