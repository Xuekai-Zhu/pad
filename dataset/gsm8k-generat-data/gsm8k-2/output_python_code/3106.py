def solution():
    """Cathy and Chris got summer jobs at the cake shop and were supposed to work 20 hours per week each for 2 months. During that time, Chris got sick for one week and Cathy took her shifts. If there are four weeks in a month, how many hours did Cathy work during the 2 months?"""
    hours_per_week = 20
    total_weeks = 8
    sick_week = 1
    chris_hours = (total_weeks - sick_week) * hours_per_week
    cathy_hours = chris_hours + hours_per_week
    result = cathy_hours
    return result

print(solution())