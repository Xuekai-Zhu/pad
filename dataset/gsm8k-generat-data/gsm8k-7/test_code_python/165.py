def solution():
    distance_to_destination = 55
    distance_back = distance_to_destination + 10

    time_to_destination = distance_to_destination * 2
    time_back = distance_back * 2
    total_driving_time = time_to_destination + time_back

    total_time = (total_driving_time / 60) + 2  # convert driving time to hours and add 2 hours for stay

    result = total_time
    return result

print(solution())