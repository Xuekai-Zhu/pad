def solution():
    """Hank reads the newspaper every morning, 5 days a week for 30 minutes. He reads part of a novel every evening, 5 days a week, for 1 hour. He doubles his reading time on Saturday and Sundays. How many minutes does Hank spend reading in 1 week?"""
    newspaper_minutes_per_day = 30
    newspaper_days_per_week = 5
    novel_minutes_per_day = 60
    novel_days_per_week = 5
    novel_minutes_on_weekend = novel_minutes_per_day * 2
    total_newspaper_minutes = newspaper_minutes_per_day * newspaper_days_per_week
    total_novel_minutes = (novel_minutes_per_day * novel_days_per_week) + (novel_minutes_on_weekend * 2)
    total_minutes = total_newspaper_minutes + total_novel_minutes
    result = total_minutes
    return result

print(solution())