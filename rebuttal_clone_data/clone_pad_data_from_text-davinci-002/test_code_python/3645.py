def solution():
    miles_to_work = 14
    mpg_car = 35
    mpg_motorcycle = 35
    gas_price = 3.75
    car_toll = 12.50
    motorcycle_toll = 7
    trips_by_car = 3
    trips_by_motorcycle = 2
    car_mileage = miles_to_work * trips_by_car
    motorcycle_mileage = miles_to_work * trips_by_motorcycle
    car_cost = (car_mileage / mpg_car) * gas_price + car_toll * trips_by_car
    motorcycle_cost = (motorcycle_mileage / mpg_motorcycle) * gas_price + motorcycle_toll * trips_by_motorcycle
    total_cost = car_cost + motorcycle_cost
    result = total_cost
    return result

print(solution())