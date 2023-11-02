def solution():
    car_engine = 2457
    car_oil = 25
    car_tires = 467
    car_detailing = 79
    total_spent = car_engine + car_oil + car_tires + car_detailing
    result = total_spent - car_engine
    return result

print(solution())