def solution():
    total_minutes = 12 * 60  # converting 8:00 PM to minutes
    start_time = 7 * 60  # converting 7:00 AM to minutes

    # Calculate the total time spent on stops
    total_stop_time = 25 + 10 + 25

    # Calculate the total time spent on the road
    total_road_time = total_minutes - start_time - total_stop_time

    # Convert total road time from minutes to hours
    hours_on_road = total_road_time / 60
    result = hours_on_road
    return result

print(solution())