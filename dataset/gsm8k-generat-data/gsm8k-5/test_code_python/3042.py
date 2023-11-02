def solution():
    total_distance = 420 + 273  # Total distance from Salt Lake City to Los Angeles
    total_time = 11  # Andy wants to complete the drive in 11 hours
    time_to_drive_to_vegas = 420 / speed_to_drive_to_vegas  # Time required to drive from Salt Lake City to Las Vegas
    time_to_drive_to_LA = 273 / speed_to_drive_to_LA  # Time required to drive from Las Vegas to Los Angeles
    remaining_time = total_time - time_to_drive_to_vegas - time_to_drive_to_LA  # Remaining time to drive

    # Calculate the required speed for remaining distance
    required_speed = (total_distance - 420 - 273) / remaining_time
    result = required_speed
    return result

print(solution())