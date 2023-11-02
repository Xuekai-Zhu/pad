def solution():
    fill_time = 15 # minutes
    drive_time = 30 # minutes
    num_trips = 6

    total_time_per_trip = (fill_time + drive_time) / 60 # convert to hours
    total_time = total_time_per_trip * num_trips

    result = total_time
    return result

print(solution())