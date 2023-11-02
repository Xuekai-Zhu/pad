def solution():
    camera_price = 110
    frame_price = 120
    discount_percent = 5
    total_price = (camera_price * 2) + (frame_price * 3)
    discount_amount = total_price * (discount_percent / 100)
    final_price = total_price - discount_amount
    result = final_price
    return result

print(solution())