def solution():
    car_price = 5200
    inspection_price = car_price / 10
    headlight_price = 80
    tire_price = headlight_price * 3
    offer1 = car_price
    offer2 = car_price - inspection_price + headlight_price + tire_price
    difference = offer1 - offer2
    result = difference
    return result

print(solution())