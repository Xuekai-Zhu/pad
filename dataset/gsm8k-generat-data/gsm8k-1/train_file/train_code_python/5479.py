def solution():
    """Helga works for a newspaper company. She can write 5 articles every 30 minutes, and she usually works 4 hours a day 5 days a week. If Helga worked an extra 2 hours last Thursday, and an extra 3 hours last Friday, how many articles was she able to write this week?"""
    articles_per_interval = 5
    interval_time_in_minutes = 30
    hours_per_day = 4
    days_per_week = 5
    total_work_hours = (hours_per_day * days_per_week) + 2 + 3 # extra hours worked
    total_work_minutes = total_work_hours * 60
    intervals = total_work_minutes // interval_time_in_minutes
    total_articles = intervals * articles_per_interval
    result = total_articles
    return result

print(solution())