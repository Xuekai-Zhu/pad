def solution():
    # Calculate the total time spent on homework
    total_homework_time = (45 + 30 + 50 + 25) / 60  # convert all homework times to hours
    # Calculate the time left for the special project
    time_left = 3 - total_homework_time  # subtract the total homework time from the available time
    result = time_left
    return result

print(solution())