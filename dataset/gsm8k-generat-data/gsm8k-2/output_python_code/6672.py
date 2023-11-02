def solution():
    """Sherman has a 30-minute commute to the office and a 30-minute commute home every day. On the weekends, he spends 2 hours, each day, driving his kids to their different activities. How many hours does Sherman drive a week?"""
    daily_commute = 1  # in hours
    weekend_drive = 2 * 2  # in hours
    weekly_drive = daily_commute * 5 + weekend_drive
    result = weekly_drive
    return result

print(solution())