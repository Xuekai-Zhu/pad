def solution():
    bus_time = 40  # The bus takes 40 minutes to drive 80 miles to the beach
    bus_speed = 80 / (bus_time / 60)  # Calculate the speed of the bus in miles per hour
    car_speed = bus_speed * 60 / 55  # Calculate the speed of the car in miles per hour
    car_time = (2 * 80) / car_speed  # Calculate the time it takes for the car to make a round trip in hours
    car_minutes = car_time * 60  # Convert the time to minutes
    result = car_minutes
    return result

print(solution())