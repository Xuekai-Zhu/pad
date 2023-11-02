def solution():
    """The red car is 40% cheaper than the blue car. The price of the blue car is $100. How much do both cars cost?"""
    blue_car_price = 100
    red_car_price = 0.6 * blue_car_price
    total_price = blue_car_price + red_car_price
    result = total_price
    return result

print(solution())