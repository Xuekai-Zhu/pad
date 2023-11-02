def solution():
    # Number of things to do for each task
    cleaning_tasks = 7
    shower_tasks = 1
    dinner_tasks = 4

    # Total number of tasks on Trey's list
    total_tasks = cleaning_tasks + shower_tasks + dinner_tasks

    # Total time required in minutes
    total_time_minutes = total_tasks * 10

    # Convert to hours
    total_time_hours = total_time_minutes / 60

    result = total_time_hours
    return result

print(solution())