def solution():
    
    peach_price = 2
    plum_price = 1
    apple_price = 3
    peach_weight = 6
    plum_weight = 8
    apple_weight = 6
    total_peach_price = peach_price * peach_weight
    total_plum_price = plum_price * plum_weight
    total_apple_price = apple_price * apple_weight
    total_price = total_peach_price + total_plum_price + total_apple_price
    result = total_price
    return result

print(solution())