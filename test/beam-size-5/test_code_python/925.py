def solution():
    
    bus_speed = 60
    bus_time = 5
    car_speed = 30
    car_time = 8
    bus_distance = bus_speed * bus_time
    car_distance = car_speed * car_time
    difference = bus_distance - car_distance
    result = difference
    return result

print(solution())