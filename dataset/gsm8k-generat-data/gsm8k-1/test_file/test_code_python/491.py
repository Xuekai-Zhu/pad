def solution():
    """Charisma works for 8 hours every day. She has a timer to remind her to get up and walk for 5 minutes every hour she’s at work. After 5 days at the office, how many minutes has she walked?"""
    hours_per_day = 8
    minutes_walking_per_hour = 5
    days_at_office = 5
    total_hours_at_office = hours_per_day * days_at_office
    total_minutes_walking = total_hours_at_office * minutes_walking_per_hour
    result = total_minutes_walking
    return result

print(solution())