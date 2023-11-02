def solution():
    
    bike_time = 30
    bus_time = bike_time + 10
    friend_time = bike_time - (2/3 * bike_time)
    total_time = bike_time + (3 * bus_time) + friend_time
    result = total_time
    return result

print(solution())