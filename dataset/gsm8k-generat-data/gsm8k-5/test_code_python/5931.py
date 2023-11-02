def solution():
    distance = 10  # distance from the house to the water park in miles
    time_at_28mph = 0.25 / 2  # time spent driving at 28 mph (half of 30 minutes)
    time_at_60mph = 0.25 / 2  # time spent driving at 60 mph (half of 30 minutes)

    # Calculate the total distance traveled at 28 mph
    distance_at_28mph = time_at_28mph * 28

    # Calculate the remaining distance to be traveled at 60 mph
    remaining_distance = distance - distance_at_28mph

    # Calculate the time it takes to travel the remaining distance at 60 mph
    time_at_60mph = remaining_distance / 60

    # Calculate the total time it takes to travel to the water park
    total_time = time_at_28mph + time_at_60mph

    # Calculate how long it takes to bike to the water park
    bike_speed = 11  # Jake can bike 11 miles per hour
    bike_time = distance / bike_speed

    # Calculate the total time it takes to get to the water park by biking
    total_bike_time = bike_time + total_time
    result = total_bike_time
    return result

print(solution())