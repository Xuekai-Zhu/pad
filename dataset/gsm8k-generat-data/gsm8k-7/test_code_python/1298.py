def solution():
    mountain_time = 3  # hours
    central_time = 4  # hours
    eastern_time = 2  # hours
    additional_time = 2  # hours (for the next day in each time zone)

    # Calculate the total time the plane spent hovering in each time zone during the first day
    total_time_first_day = mountain_time + central_time + eastern_time

    # Calculate the total time the plane spent hovering in each time zone during the second day
    total_time_second_day = (mountain_time + additional_time) + (central_time + additional_time) + (eastern_time + additional_time)

    # Calculate the total time the plane spent hovering in all time zones over the two days
    total_time = total_time_first_day + total_time_second_day
    result = total_time
    return result

print(solution())