def solution():
    # Convert flight time to minutes
    flight_time = 11 * 60 + 20

    # Calculate total time spent on activities
    total_activity_time = 2 * 60 + 4 * 60 + 30 + 40 + 1 * 60 + 10

    # Calculate time left for a nap
    time_left = flight_time - total_activity_time

    # Convert time back to hours
    time_left_hours = time_left / 60

    # Round to two decimal places
    result = round(time_left_hours, 2)
    return result

print(solution())