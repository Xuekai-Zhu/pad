def solution():
    # Calculate the distance Christina will drive
    christina_distance = 210 - (40 * 3)

    # Calculate the time Christina will drive
    christina_time = christina_distance / 30

    # Convert the time to minutes
    christina_time_minutes = christina_time * 60

    result = christina_time_minutes
    return result

print(solution())