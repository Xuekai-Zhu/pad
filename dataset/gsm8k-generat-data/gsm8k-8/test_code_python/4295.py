def solution():
    # Define the total distance and the speed
    total_distance = 300
    speed = 50

    # Calculate the total time without rest
    time_without_rest = total_distance / speed

    # Calculate the number of rest stops needed and the total time for rest
    rest_stops = time_without_rest // 2
    total_rest_time = rest_stops * 0.5

    # Calculate the total time with rest
    total_time = time_without_rest + total_rest_time

    result = total_time
    return result

print(solution())