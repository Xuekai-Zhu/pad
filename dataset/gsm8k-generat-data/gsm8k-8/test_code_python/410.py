def solution():
    # Define the record and Mark's jumping speed
    record = 54000
    jump_speed = 3

    # Calculate the total time in seconds
    total_time_seconds = record / jump_speed

    # Convert seconds to hours
    total_time_hours = total_time_seconds / 3600
    result = total_time_hours
    return result

print(solution())