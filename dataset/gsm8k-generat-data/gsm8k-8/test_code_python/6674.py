def solution():
    # Define the start and end times in minutes
    start_time = 7 * 60
    end_time = 20 * 60

    # Calculate the total time spent on the road in minutes
    time_on_road = end_time - start_time - 25 - 10 - 25

    # Convert the total time to hours
    time_on_road_hours = time_on_road / 60

    result = time_on_road_hours
    return result

print(solution())