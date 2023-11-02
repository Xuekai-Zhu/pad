def solution():
    # Calculate the total distance biked during the workweek
    work_distance = 2 * 20 * 5

    # Calculate the time spent biking during the workweek
    work_time = work_distance / 25

    # Calculate the time spent biking during the weekend
    weekend_time = 200 / 25

    # Calculate the total time spent biking during the week
    total_time = work_time + weekend_time
    result = total_time
    return result

print(solution())