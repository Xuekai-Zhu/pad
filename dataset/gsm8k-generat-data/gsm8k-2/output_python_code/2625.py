def solution():
    """Mark wants to order a pair of slippers for his wife with her initials embroidered on top. The slippers are currently $50.00 and are 10% off. The embroidery will be $5.50 per shoe and shipping is a flat rate of $10.00. How much will the slippers cost?"""
    slipper_price = 50
    discount_percentage = 0.1
    embroidery_price_per_shoe = 5.5
    shipping_price = 10
    slipper_price_with_discount = slipper_price - (slipper_price * discount_percentage)
    total_embroidery_price = embroidery_price_per_shoe * 2
    total_price = slipper_price_with_discount + total_embroidery_price + shipping_price
    result = total_price
    return result

print(solution())