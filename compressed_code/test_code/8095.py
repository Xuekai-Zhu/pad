def solution():
    
    bikes = 20
    cars = 10
    motorcycles = 5
    wheels_per_bike = 2
    wheels_per_car = 4
    wheels_per_motorcycle = 2
    total_wheels = (bikes * wheels_per_bike) + (cars * wheels_per_car) + (motorcycles * wheels_per_motorcycle)
    result = total_wheels
    return result

print(solution())