def solution():
    """Venny spent $15000 on a used car which cost 40% of the original price. What was the original price of the car?"""
    used_car_price = 15000
    percentage_of_original_price = 40
    original_price = used_car_price / (percentage_of_original_price / 100)
    result = original_price
    return result

print(solution())