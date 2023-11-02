def solution():
    red_stamps = 20
    blue_stamps = 80
    yellow_stamps = 7
    sold_red_stamps = 20
    sold_blue_stamps = 80
    total_price = 100
    price_red_stamps = 1.1
    price_blue_stamps = 0.8
    price_yellow_stamps = (total_price - (sold_red_stamps * price_red_stamps) - (sold_blue_stamps * price_blue_stamps)) / yellow_stamps
    result = price_yellow_stamps
    return result

print(solution())