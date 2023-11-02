def solution():
    
    bed_frame_price = 75
    bed_price = 10 * bed_frame_price
    discount_percent = 20
    discounted_price = (bed_frame_price + bed_price) * (1 - discount_percent / 100)
    result = discounted_price
    return result

print(solution())