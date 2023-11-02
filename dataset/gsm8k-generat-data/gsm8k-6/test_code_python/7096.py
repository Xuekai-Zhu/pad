def solution():
    original_price = 15.00  
    discount = 0.20  # 20% off
    sale_price = original_price * (1-discount)  # price after discount
    num_bottles = 3
    total_price = (num_bottles * sale_price) - (3 * 2.00)  # subtracting the coupon value from total price
    result = total_price
    return result

print(solution())