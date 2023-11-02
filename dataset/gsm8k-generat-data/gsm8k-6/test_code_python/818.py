def solution():
    # Calculate the total number of tasks on Trey's list
    total_tasks = 7 + 1 + 4

    # Calculate the total time to complete all tasks
    total_time = total_tasks * 10  # assuming each task takes 10 minutes to complete

    # Convert total time to hours
    total_time_hours = total_time / 60

    result = total_time_hours
    return result

print(solution())