def solution():
    """Ken buys gummy vitamins. They are usually $15.00 per bottle at his grocery store, but they are currently 20% off. On top of that, he has 3 $2.00 coupons. How much will 3 bottles cost?"""
    # Define the regular price of the gummy vitamins
    regular_price = 15.00

    # Calculate the sale price of the gummy vitamins with the 20% discount
    sale_price = regular_price * 0.8

    # Calculate the final price of one bottle with the coupon
    final_price = sale_price - 2.00

    # Calculate the final cost of 3 bottles with the coupons
    total_cost = final_price * 3

    # return the result
    result = total_cost
    return result

print(solution())