def solution():
    """Ralph has $54.00 worth of products in his cart.  At the register, he asks if he could have a 20% discount on an item with a small issue.  This item is $20.00 to start.  They agree.   Ralph also has a 10% coupon on his purchase, which he uses after the 20% discount on the item with the small issue.  How much will all of his items cost?"""
    # Define the starting price of the item with a small issue
    ITEM_PRICE = 20

    # Calculate the price after the 20% discount
    discounted_price = ITEM_PRICE * 0.8

    # Define the total amount before the coupon
    total_before_coupon = 54 + ITEM_PRICE

    # Calculate the total amount after the discount and before the coupon
    total_after_discount = total_before_coupon - ITEM_PRICE + discounted_price

    # Calculate the final total after applying the coupon
    final_total = total_after_discount * 0.9

    # Display the final total
    result = final_total
    return result

print(solution())