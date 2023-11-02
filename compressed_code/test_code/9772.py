def solution():
    
    purchase_price = 250
    discount_rate = 10
    discount_threshold = 100
    dollars_off = (purchase_price // discount_threshold) * discount_rate
    final_price = purchase_price - dollars_off
    result = final_price
    return result

print(solution())