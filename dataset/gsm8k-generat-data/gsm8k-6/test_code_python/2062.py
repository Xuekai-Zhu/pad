def solution():
    # Calculate the total time spent by Joan
    total_time = 30 + 25 + 38  # minutes spent on piano, writing music, and reading

    # Calculate the time left for using the finger exerciser
    time_left = (2 * 60) - total_time  # 2 hours (120 minutes) minus total time spent
    result = time_left
    return result

print(solution())