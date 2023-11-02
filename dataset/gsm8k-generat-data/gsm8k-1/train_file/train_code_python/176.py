def solution():
    """James decides to replace his car. He sold his $20,000 car for 80% of its value and then was able to haggle to buy a $30,000 sticker price car for 90% of its value. How much was he out of pocket?"""
    sold_car_price = 20000 * 0.8
    bought_car_price = 30000 * 0.9
    out_of_pocket = bought_car_price - sold_car_price
    result = out_of_pocket
    return result

print(solution())