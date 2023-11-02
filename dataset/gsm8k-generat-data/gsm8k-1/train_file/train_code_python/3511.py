def solution():
    """Roy spends 2 hours on sports activities in school every day. He goes to school 5 days a week. If he missed 2 days within a week, how many hours did he spend on sports in school that week?"""
    hours_per_day = 2
    days_per_week = 5 - 2  # subtract 2 days missed
    total_hours = hours_per_day * days_per_week
    result = total_hours
    return result

print(solution())