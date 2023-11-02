def solution():
    chris_speed = 3
    distance_to_school = 9

    # Calculate the time it takes for Chris to walk to school
    time_for_chris = distance_to_school / chris_speed

    # Calculate the distance Mark walked before going back home
    mark_dist_to_turnaround = 3

    # Calculate the time it takes for Mark to reach his home
    time_for_mark_to_home = mark_dist_to_turnaround / chris_speed

    # Calculate the total time it takes for Mark to return home and then reach the school
    total_time_for_mark = 2 * time_for_mark_to_home + time_for_chris

    # Calculate the difference in time between Mark and Chris
    extra_time_for_mark = total_time_for_mark - time_for_chris

    result = extra_time_for_mark
    return result

print(solution())