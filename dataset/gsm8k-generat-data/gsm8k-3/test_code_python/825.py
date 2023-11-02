def solution():
    """James decides to buy a new bed and bed frame.  The bed frame is $75 and the bed is 10 times that price.  He gets a deal for 20% off.  How much does he pay for everything?"""
    # Define the price of the bed frame and bed
    FRAME_PRICE = 75
    BED_PRICE = FRAME_PRICE * 10

    # Calculate the total price before the discount
    total_price = FRAME_PRICE + BED_PRICE

    # Calculate the discount amount
    discount = total_price * 0.2

    # Calculate the final price after the discount
    final_price = total_price - discount

    # Display the final price
    result = final_price
    return result

print(solution())