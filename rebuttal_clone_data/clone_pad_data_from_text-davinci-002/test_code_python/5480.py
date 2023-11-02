def solution():
    articles_per_30_min = 5
    work_hours_per_day = 4
    work_days_per_week = 5
    extra_work_hours_thursday = 2
    extra_work_hours_friday = 3
    total_extra_work_hours = extra_work_hours_thursday + extra_work_hours_friday
    total_work_hours = total_extra_work_hours + (work_hours_per_day * work_days_per_week)
    total_articles = total_work_hours * articles_per_30_min
    result = total_articles
    
    return result

print(solution())