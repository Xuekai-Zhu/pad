def solution():
    time_per_trip = (15/60) + (30/60)  # time to fill up the car (15min) + time to drive (30min), both converted to hours
    total_time = time_per_trip * 6  # total time for 6 trips
    result = total_time
    return result

print(solution())