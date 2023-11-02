def solution():
    """Tom dances 4 times a week for 2 hours at a time and does this every year for 10 years. How many hours did he dance?"""
    weekly_hours = 4 * 2
    yearly_hours = weekly_hours * 52
    total_hours = yearly_hours * 10
    result = total_hours
    return result

print(solution())