def solution():
    original_car_price = 30000
    sale_price = original_car_price * 0.8
    new_car_price = 40000
    money_saved = original_car_price - new_car_price
    percent_saved = (money_saved / original_car_price) * 100
    result = percent_saved
    return result

print(solution())