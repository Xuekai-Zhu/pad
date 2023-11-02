def solution():
    """Ralph has $54.00 worth of products in his cart. At the register, he asks if he could have a 20% discount on an item with a small issue. This item is $20.00 to start. They agree. Ralph also has a 10% coupon on his purchase, which he uses after the 20% discount on the item with the small issue. How much will all of his items cost?"""
    original_cost = 54
    discount_percent = 20
    item_cost = 20
    item_discount = item_cost * (discount_percent/100)
    discounted_item_cost = item_cost - item_discount
    subtotal = original_cost - item_cost + discounted_item_cost
    coupon_percent = 10
    total_discount = subtotal * (coupon_percent/100)
    total_cost = subtotal - total_discount
    result = total_cost
    return result

print(solution())