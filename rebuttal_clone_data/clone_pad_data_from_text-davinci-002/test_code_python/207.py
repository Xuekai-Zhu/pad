def solution():
    """John volunteers at a shelter twice a month for 3 hours at a time. How many hours does he volunteer per year?"""
    visits_per_month = 2
    hours_per_visit = 3
    months_per_year = 12
    total_hours = visits_per_month * hours_per_visit * months_per_year
    result = total_hours
    return result

print(solution())