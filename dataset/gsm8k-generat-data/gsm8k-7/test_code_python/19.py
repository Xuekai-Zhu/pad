def solution():
    num_workdays = 5
    work_distance = 20
    weekend_distance = 200
    biking_speed = 25

    # Calculate the total distance Tim bikes during the workweek
    workweek_distance = num_workdays * 2 * work_distance

    # Calculate the total biking time for the workweek
    workweek_time = workweek_distance / biking_speed

    # Calculate the biking time for the weekend
    weekend_time = weekend_distance / biking_speed

    # Calculate the total biking time for the week
    total_time = workweek_time + weekend_time
    result = total_time
    return result

print(solution())