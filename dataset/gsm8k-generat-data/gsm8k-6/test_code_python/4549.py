def solution():
    # Calculate the time taken by the car to make a one-way trip to the beach
    bus_time = 40  # minutes taken by bus to drive to the beach
    bus_speed = 80/bus_time  # speed of the bus
    car_speed = bus_speed  # car and bus cover the same distance in the same time
    car_time = bus_time - 5  # car takes 5 fewer minutes than the bus to make the same trip
    car_distance = car_speed * (car_time/60) * 80  # distance covered by the car to make the one-way trip to the beach

    # Calculate the total time taken by the car to make a round trip
    round_trip_time = (car_time * 2) + ((car_distance * 2) / car_speed) * 60
    result = round_trip_time
    return result

print(solution())