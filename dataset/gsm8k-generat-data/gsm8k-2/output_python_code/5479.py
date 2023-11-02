def solution():
    """Helga works for a newspaper company. She can write 5 articles every 30 minutes, and she usually works 4 hours a day 5 days a week. If Helga worked an extra 2 hours last Thursday, and an extra 3 hours last Friday, how many articles was she able to write this week?"""
    articles_per_half_hour = 5
    half_hours_per_day = 2
    hours_per_day = 4
    days_per_week = 5
    regular_hours = half_hours_per_day * hours_per_day * days_per_week
    extra_hours = 2 + 3
    total_hours = regular_hours + extra_hours
    total_articles = total_hours * articles_per_half_hour
    result = total_articles
    return result

print(solution())