def solution():
    
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