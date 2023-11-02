def solution():
    """Eunice spent $7500 on a used car, which is 25% less than the original price. What was the original price of the car?"""
    used_car_price = 7500
    percent_less = 0.25
    original_price = used_car_price / (1 - percent_less)
    result = original_price
    return result

print(solution())