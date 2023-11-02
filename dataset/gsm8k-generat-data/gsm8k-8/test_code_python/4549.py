def solution():
    # Calculate the time it takes for the car to make a one-way trip
    bus_time = 40
    bus_speed = 80 / 40
    car_speed = bus_speed * 60 / 55
    car_time = 80 / car_speed

    # Calculate the round-trip time for the car
    round_trip_time = car_time * 2
    result = round_trip_time
    return result

print(solution())