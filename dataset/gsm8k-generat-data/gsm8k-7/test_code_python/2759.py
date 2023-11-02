def solution():
    bike_days_per_week = 1
    bus_days_per_week = 3
    friend_days_per_week = 1

    bike_time = 30
    bus_time = bike_time + 10
    friend_time = bike_time - (bike_time * (2/3))

    # Calculate the total time for biking
    total_bike_time = bike_days_per_week * bike_time

    # Calculate the total time for taking the bus
    total_bus_time = bus_days_per_week * bus_time

    # Calculate the total time for getting a ride from a friend
    total_friend_time = friend_days_per_week * friend_time

    # Calculate the total time spent commuting to work
    total_time = total_bike_time + total_bus_time + total_friend_time

    # Convert total_time to minutes
    total_time_in_minutes = total_time * 60
    result = total_time_in_minutes
    return result

print(solution())