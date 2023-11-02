def solution():
    distance = 2790
    speed = 62
    rest_time = 0.5  # 30 minutes in hours
    rest_interval = 5  # every 5 hours

    # Calculate the total time spent driving
    total_drive_time = distance / speed

    # Calculate the total number of breaks taken
    num_breaks = total_drive_time // rest_interval
    
    # Calculate the total time spent on breaks
    total_rest_time = num_breaks * rest_time

    # Add the time spent looking for the hotel
    total_time = total_drive_time + total_rest_time + 0.5  # 30 minutes in hours
    result = total_time
    return result

print(solution())