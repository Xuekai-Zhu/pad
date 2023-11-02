def solution():
    """Hank reads the newspaper every morning, 5 days a week for 30 minutes. He reads part of a novel every evening, 5 days a week, for 1 hour. He doubles his reading time on Saturday and Sundays. How many minutes does Hank spend reading in 1 week?"""
    newspaper_minutes_per_week = 5 * 30
    novel_minutes_per_week = 5 * 60
    weekend_newspaper_minutes = 2 * (30 * 2)
    weekend_novel_minutes = 2 * (60 * 2)
    total_minutes_per_week = newspaper_minutes_per_week + novel_minutes_per_week + weekend_newspaper_minutes + weekend_novel_minutes
    result = total_minutes_per_week
    return result

print(solution())