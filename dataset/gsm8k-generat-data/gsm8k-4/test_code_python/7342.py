def solution():
    """There's a sale at your favorite "Any item $10" retailer. If you buy 1 shirt you pay $10. If you buy 2, you get the second one at a 50% discount. If you buy 3, you get the third one at a 60% discount. How much money did you save if you bought 3 shirts?"""
    # Define the price of a single shirt
    shirt_price = 10

    # Calculate the price of buying 2 shirts with the discount
    two_shirts_price = shirt_price + (shirt_price * 0.5)

    # Calculate the price of buying 3 shirts with the discounts
    three_shirts_price = two_shirts_price + (shirt_price * 0.6)

    # Calculate the total amount saved by buying 3 shirts with the discounts
    total_savings = (shirt_price * 3) - three_shirts_price

    result = total_savings
    return result

print(solution())