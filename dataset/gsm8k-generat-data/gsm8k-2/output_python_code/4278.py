def solution():
    """Bill had to finish a project from work that was to take him 4 days. If he took 6 seven-hour naps in the four days, how long did he spend working on the project?"""
    total_work_hours = 4 * 24
    nap_hours = 6 * 7
    working_hours = total_work_hours - nap_hours
    result = working_hours
    return result

print(solution())