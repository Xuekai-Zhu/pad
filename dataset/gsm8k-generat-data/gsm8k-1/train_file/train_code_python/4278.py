def solution():
    """Bill had to finish a project from work that was to take him 4 days. If he took 6 seven-hour naps in the four days, how long did he spend working on the project?"""
    total_days = 4
    total_work_hours = total_days * 24 - (6 * 7)
    result = total_work_hours
    return result

print(solution())