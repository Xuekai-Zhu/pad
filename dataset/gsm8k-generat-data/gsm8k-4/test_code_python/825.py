def solution():
    """James decides to buy a new bed and bed frame. The bed frame is $75 and the bed is 10 times that price. He gets a deal for 20% off. How much does he pay for everything?"""
    # Define the price of the bed frame and bed
    bed_frame_price = 75
    bed_price = 750

    # Calculate the total price before discount
    total_price = bed_frame_price + bed_price

    # Calculate the amount of discount
    discount_amount = total_price * 0.2

    # Calculate the total price after discount
    total_price_after_discount = total_price - discount_amount

    result = total_price_after_discount
    return result

print(solution())