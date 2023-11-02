def solution():
    slipper_price = 50.00
    discount_percentage = 10
    embroidery_per_shoe = 5.50
    shipping_flat_rate = 10.00
 
    slipper_discount = slipper_price * (discount_percentage / 100)
    embroidery_cost = 2 * embroidery_per_shoe
    slippers_after_discount_and_embroidery = slipper_price - slipper_discount + embroidery_cost
    total_cost = slippers_after_discount_and_embroidery + shipping_flat_rate
 
    result = total_cost
    return result

print(solution())