def solution():
    # Calculate the total hours Bill had for the project
    total_hours = 4 * 24

    # Calculate the total time spent on naps
    nap_time = 6 * 7

    # Calculate the time spent working on the project
    work_time = total_hours - nap_time

    # Convert work time to days
    work_days = work_time / 24

    result = work_days
    return result

print(solution())