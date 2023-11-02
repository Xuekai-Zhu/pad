def solution():
    # Calculate the total break time in hours
    total_break_time = ((2790 / 62) // 5) * 0.5

    # Calculate the total time spent driving in hours
    total_driving_time = 2790 / 62

    # Calculate the time spent looking for the hotel in hours
    hotel_time = 0.5

    # Calculate the total travel time in hours
    total_travel_time = total_driving_time + total_break_time + hotel_time

    result = total_travel_time
    return result

print(solution())