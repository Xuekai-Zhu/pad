def solution():
    """Ayen jogs for 30 minutes every day during weekdays. This week on Tuesday, she jogged 5 minutes more and also jogged 25 minutes more on Friday. How many hours, in total, did Ayen jog this week?"""
    daily_jog_minutes = 30
    tuesday_jog_minutes = 35
    friday_jog_minutes = 55
    total_weekly_minutes = (daily_jog_minutes * 5) + tuesday_jog_minutes + friday_jog_minutes
    total_weekly_hours = total_weekly_minutes / 60
    result = total_weekly_hours
    return result

print(solution())