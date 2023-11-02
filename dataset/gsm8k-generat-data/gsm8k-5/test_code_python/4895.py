def solution():
    total_distance = 210  # The total distance is 210 miles
    friend_drive_time = 3  # Her friend drives for 3 hours
    friend_drive_distance = 40 * friend_drive_time  # Her friend drives at 40 miles per hour for 3 hours
    christina_drive_distance = total_distance - friend_drive_distance  # Christina drives the remaining distance

    # Calculate the time Christina needs to drive at 30 miles per hour
    christina_drive_time = christina_drive_distance / 30

    # Convert the time Christina drives to minutes
    minutes_driven_by_christina = christina_drive_time * 60
    result = int(minutes_driven_by_christina)
    return result

print(solution())