def solution():
    
    dish1_price = 10
    dish2_price = 13
    dish3_price = 17
    total_price = dish1_price + dish2_price + dish3_price
    tip_percent = 10
    tip_amount = total_price * (tip_percent / 100)
    result = tip_amount
    return result

print(solution())