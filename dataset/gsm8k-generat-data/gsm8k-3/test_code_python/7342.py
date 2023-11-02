def solution():
    """There's a sale at your favorite "Any item $10" retailer. If you buy 1 shirt you pay $10. If you buy 2, you get the second one at a 50% discount. If you buy 3, you get the third one at a 60% discount. How much money did you save if you bought 3 shirts?"""
    # Define the cost of each shirt
    SHIRT_PRICE = 10

    # Buy 1 shirt
    shirt1_cost = SHIRT_PRICE
    shirt1_discount = 0

    # Buy 2 shirts
    shirt2_cost = SHIRT_PRICE + (SHIRT_PRICE / 2)
    shirt2_discount = SHIRT_PRICE / 2

    # Buy 3 shirts
    shirt3_cost = SHIRT_PRICE + (SHIRT_PRICE / 2) + (SHIRT_PRICE * 0.4)
    shirt3_discount = SHIRT_PRICE * 0.6

    # Calculate the total saved by buying all 3 shirts
    total_saved = shirt1_discount + shirt2_discount + shirt3_discount

    # Display the total saved
    result = total_saved
    return result

print(solution())