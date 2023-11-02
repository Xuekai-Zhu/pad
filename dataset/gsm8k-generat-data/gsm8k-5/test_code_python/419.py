def solution():
    basketball_time = 10  # Kenny played basketball for 10 hours
    running_time = 2 * basketball_time  # Kenny ran for twice as long as he played basketball
    trumpet_time = 2 * running_time  # Kenny practiced on the trumpet for twice as long as he ran

    # Calculate the total time Kenny spent on all activities
    total_time = basketball_time + running_time + trumpet_time
    trumpet_hours = trumpet_time

    result = trumpet_hours
    return result

print(solution())