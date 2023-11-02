def solution():
    
    bike_day = 1
    bus_day = 3
    ride_day = 1
    bike_time = 30
    bus_time = bike_time + 10
    ride_time = bike_time * (1/3)
    total_time = (bike_day * bike_time) + (bus_day * bus_time) + (ride_day * ride_time)
    result = total_time
    return result

print(solution())