def solution():
    """Ken buys gummy vitamins.  They are usually $15.00 per bottle at his grocery store, but they are currently 20% off.  On top of that, he has 3 $2.00 coupons.  How much will 3 bottles cost?"""
    # Define the original price per bottle and discount percentage
    ORIGINAL_PRICE = 15.00
    DISCOUNT_PERCENTAGE = 20

    # Calculate the discounted price per bottle
    discounted_price = ORIGINAL_PRICE - (ORIGINAL_PRICE * DISCOUNT_PERCENTAGE / 100)

    # Calculate the total cost for 3 bottles, including the coupons
    total_cost = (discounted_price * 3) - (3 * 2)

    # Display the total cost
    result = total_cost
    return result

print(solution())