def solution():
    """Cathy and Chris got summer jobs at the cake shop and were supposed to work 20 hours per week each for 2 months. During that time, Chris got sick for one week and Cathy took her shifts. If there are four weeks in a month, how many hours did Cathy work during the 2 months?"""
    hours_per_week = 20
    weeks_per_month = 4
    total_weeks = 2 * weeks_per_month
    chris_sick_weeks = 1
    cathy_worked_weeks = total_weeks - chris_sick_weeks
    cathy_total_hours = cathy_worked_weeks * hours_per_week * 2
    result = cathy_total_hours
    return result

print(solution())