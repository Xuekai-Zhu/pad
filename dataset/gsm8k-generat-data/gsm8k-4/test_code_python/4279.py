def solution():
    """Bill had to finish a project from work that was to take him 4 days. If he took 6 seven-hour naps in the four days, how long did he spend working on the project?"""
    # Define the total time in hours for the project
    total_project_hours = 4 * 24

    # Calculate the total amount of time Bill spent sleeping
    total_sleep_hours = 6 * 7

    # Calculate the total amount of time Bill spent working on the project
    total_work_hours = total_project_hours - total_sleep_hours

    # return the result
    result = total_work_hours
    return result

print(solution())