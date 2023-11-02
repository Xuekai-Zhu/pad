def solution():
    # Calculate the total size of the files in megabits
    total_size = 80 + 90 + 70

    # Calculate the total time needed to download in minutes
    total_time_in_minutes = total_size / 2

    # Convert the time to hours and round to two decimal places
    total_time_in_hours = round(total_time_in_minutes / 60, 2)

    result = total_time_in_hours
    return result

print(solution())