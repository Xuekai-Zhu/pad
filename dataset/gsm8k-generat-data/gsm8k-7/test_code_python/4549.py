def solution():
    bus_time = 40  # minutes
    bus_distance = 80  # miles
    car_time_diff = 5  # minutes

    # Calculate the speed of the bus
    bus_speed = bus_distance / (bus_time / 60)

    # Calculate the time it takes the car to travel to the beach
    car_time_to_beach = (bus_distance / (bus_speed * 60)) * 60 - car_time_diff

    # Calculate the time it takes the car to make a round trip
    round_trip_time = (car_time_to_beach * 2) + (bus_time * 2)

    result = round_trip_time
    return result

print(solution())