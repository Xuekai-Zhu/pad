def solution():
    
    red_stamps = 20
    blue_stamps = 80
    yellow_stamps = 7
    red_price = 1.1
    blue_price = 0.8
    total_earned = (red_stamps * red_price) + (blue_stamps * blue_price)
    yellow_price = (100 - total_earned) / yellow_stamps
    result = yellow_price
    return result

print(solution())