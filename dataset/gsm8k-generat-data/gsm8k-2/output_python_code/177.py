def solution():
    """James decides to replace his car. He sold his $20,000 car for 80% of its value and then was able to haggle to buy a $30,000 sticker price car for 90% of its value. How much was he out of pocket?"""
    initial_car_value = 20000
    sold_car_value = initial_car_value * 0.8
    new_car_value = 30000 * 0.9
    out_of_pocket = new_car_value - sold_car_value
    result = out_of_pocket
    return result

print(solution())