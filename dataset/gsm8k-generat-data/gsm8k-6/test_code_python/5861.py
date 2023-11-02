def solution():
    item_price = 20.00
    item_discount = 0.20
    cart_total = 54.00
    coupon_discount = 0.10

    # Calculate the discount on the item with the small issue
    item_discount_amount = item_discount * item_price
    discounted_item_price = item_price - item_discount_amount

    # Calculate the new cart total with the discounted item
    new_cart_total = cart_total - item_discount_amount

    # Calculate the final cost after applying the coupon discount
    final_cost = new_cart_total - (new_cart_total * coupon_discount)
    result = final_cost
    return result

print(solution())