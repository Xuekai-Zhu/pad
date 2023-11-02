def solution():
    distance = 200
    time_with_traffic = 5
    time_without_traffic = 4

    # Calculate the average speed with traffic
    speed_with_traffic = distance/time_with_traffic

    # Calculate the average speed without traffic
    speed_without_traffic = distance/time_without_traffic

    # Calculate the difference in average speeds
    speed_difference = speed_with_traffic - speed_without_traffic
    result = speed_difference
    return result

print(solution())