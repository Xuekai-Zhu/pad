def solution():
    
    car_washes = 3
    car_price = 10
    lawn_mows = 2
    lawn_price = 13
    bike_price = 80
    total_earned = (car_washes * car_price) + (lawn_mows * lawn_price)
    money_needed = bike_price - total_earned
    result = money_needed
    return result

print(solution())