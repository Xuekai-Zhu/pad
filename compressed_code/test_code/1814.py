def solution():
    
    little_car_price = 5
    total_earned = 45
    little_cars_sold = 3
    total_little_cars_price = little_cars_sold * little_car_price
    lego_set_price = total_earned - total_little_cars_price
    result = lego_set_price
    return result

print(solution())