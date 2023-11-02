def solution():
    # Calculate the time spent driving without breaks
    total_time = 2790 / 62  # divide the distance by the driving speed

    # Calculate the number of breaks taken
    num_breaks = total_time // 5

    # Calculate the total time spent on breaks
    total_break_time = num_breaks * 0.5  # 30 minutes = 0.5 hours

    # Add the time spent on breaks and finding the hotel to the driving time
    total_trip_time = total_time + total_break_time + 0.5  # adding 30 minutes for finding the hotel

    result = total_trip_time
    return result

print(solution())