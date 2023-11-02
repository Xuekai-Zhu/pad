def solution():
    # Calculate the total time spent on each trip
    trip_time = 15 + 30 + 15  # 15 minutes to load, 30 minutes to drive, 15 minutes to unload

    # Calculate the total time spent on all 6 trips
    total_time = trip_time * 6

    # Convert total time to hours
    hours_spent = total_time / 60

    result = hours_spent
    return result

print(solution())