def solution():
    """A bus travels 60 miles per hour for 5 hours. A car travels 30 miles per hour for 8 hours. How much farther did the bus go than the car, in miles?"""
    bus_speed = 60
    car_speed = 30
    bus_time = 5
    car_time = 8
    bus_distance = bus_speed * bus_time
    car_distance = car_speed * car_time
    difference = bus_distance - car_distance
    result = difference
    return result

print(solution())