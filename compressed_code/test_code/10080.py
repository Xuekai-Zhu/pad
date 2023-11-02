def solution():
    
    articles_per_interval = 5
    interval_time_in_minutes = 30
    hours_per_day = 4
    days_per_week = 5
    total_work_hours = (hours_per_day * days_per_week) + 2 + 3 
    total_work_minutes = total_work_hours * 60
    intervals = total_work_minutes // interval_time_in_minutes
    total_articles = intervals * articles_per_interval
    result = total_articles
    return result

print(solution())