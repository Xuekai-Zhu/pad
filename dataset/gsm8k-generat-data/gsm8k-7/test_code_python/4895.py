def solution():
    total_distance = 210
    christina_speed = 30
    friend_speed = 40
    friend_drive_time = 3

    # Calculate the remaining distance after the friend drives for 3 hours
    remaining_distance = total_distance - (friend_speed * friend_drive_time)

    # Calculate the time it takes for Christina to drive the remaining distance
    christina_drive_time = remaining_distance / christina_speed

    # Convert the time to minutes
    christina_drive_time_minutes = christina_drive_time * 60

    result = christina_drive_time_minutes
    return result

print(solution())