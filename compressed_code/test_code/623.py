def solution():
    
    bed_frame_price = 75
    bed_price = 10 * bed_frame_price
    total_price = bed_frame_price + bed_price
    discount = 0.2 * total_price
    final_price = total_price - discount
    result = final_price
    return result

print(solution())