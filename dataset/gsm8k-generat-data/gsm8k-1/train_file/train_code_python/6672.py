def solution():
    """Sherman has a 30-minute commute to the office and a 30-minute commute home every day. On the weekends, he spends 2 hours, each day, driving his kids to their different activities. How many hours does Sherman drive a week?"""
    daily_commute = 1  # 30 minutes each way = 1 hour per day
    weekend_activities = 2 * 2  # 2 hours each day, both Saturday and Sunday
    total_drive_time = (daily_commute * 5) + weekend_activities
    result = total_drive_time
    return result

print(solution())