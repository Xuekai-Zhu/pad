def solution():
    # Calculate the price of the item with the small issue after the 20% discount
    discounted_item_price = 20 - (20 * 0.2)

    # Calculate the total price of the items before any discounts
    total_price_before_discounts = 54 + 20

    # Calculate the price of the items after the 20% discount on the item with the small issue
    total_price_after_item_discount = total_price_before_discounts - discounted_item_price

    # Calculate the price of the items after the 10% discount coupon is applied
    total_price_after_coupon_discount = total_price_after_item_discount - (total_price_after_item_discount * 0.1)

    result = total_price_after_coupon_discount
    return result

print(solution())