def solution():
    """"Ralph has $54.00 worth of products in his cart. At the register, he asks if he could have a 20% discount on an item with a small issue. This item is $20.00 to start. They agree. Ralph also has a 10% coupon on his purchase, which he uses after the 20% discount on the item with the small issue. How much will all of his items cost?"""
    original_price = 54
    item_price = 20
    discount = 0.2
    coupon = 0.1

    # Calculate the discounted price of the item with a small issue
    discounted_item_price = item_price - (item_price * discount)

    # Calculate the total price of all items before coupon
    total_price_before_coupon = original_price + discounted_item_price

    # Calculate the final price after coupon
    final_price = total_price_before_coupon - (total_price_before_coupon * coupon)

    result = final_price
    return result

print(solution())