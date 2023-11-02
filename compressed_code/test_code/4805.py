def solution():
    
    treadmill_price = 1350
    discount_percentage = 30
    discount_amount = treadmill_price * (discount_percentage / 100)
    discounted_price = treadmill_price - discount_amount
    plates_price = 2 * 50
    total_price = discounted_price + plates_price
    result = total_price
    return result

print(solution())