def solution():
    # Calculate the length of the video when watched at the average speed
    average_speed_length = 100

    # Calculate the length of the video when watched at two times the average speed
    double_speed_length = 100 / 2

    # Calculate the total number of hours Lila watched
    lila_hours = double_speed_length * 6

    # Calculate the total number of hours Roger watched
    roger_hours = average_speed_length * 6

    # Calculate the total number of hours they watched together
    total_hours = lila_hours + roger_hours
    result = total_hours
    return result

print(solution())