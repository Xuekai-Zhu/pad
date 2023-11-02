def solution():
    """Based on a 2008 study, children 6–11 years old spend 45 minutes each day watching television. How many hours do these children watch television in 2 weeks if they are allowed to watch television 4 days a week?"""
    minutes_per_day = 45
    days_per_week = 4
    weeks = 2
    total_minutes = minutes_per_day * days_per_week * weeks
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())