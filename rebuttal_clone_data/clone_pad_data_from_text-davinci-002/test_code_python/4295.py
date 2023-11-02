def solution():
    total_distance = 300
    rate = 50
    stops_interval = 2
    stop_time = 30
    travel_time = total_distance / rate
    total_time = travel_time + (stops_interval * stop_time / 60)
    result = total_time
    return result

print(solution())