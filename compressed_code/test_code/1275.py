def solution():
    
    small_bulb_price = 8
    large_bulb_price = 12
    small_bulb_count = 3
    large_bulb_count = 1
    total_price = (small_bulb_price * small_bulb_count) + (large_bulb_price * large_bulb_count)
    remaining_money = 60 - total_price
    result = remaining_money
    return result

print(solution())