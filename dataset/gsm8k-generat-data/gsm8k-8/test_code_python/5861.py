def solution():
    # Find the discounted price of the item with the small issue
    item_price = 20
    discount_percent = 20
    discounted_price = item_price - (item_price * (discount_percent/100))

    # Calculate the subtotal before applying the coupon
    subtotal = 54 + discounted_price

    # Apply the 10% coupon to the subtotal
    coupon_percent = 10
    total = subtotal - (subtotal * (coupon_percent/100))

    result = total
    return result

print(solution())