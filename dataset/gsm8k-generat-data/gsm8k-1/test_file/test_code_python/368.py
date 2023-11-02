def solution():
    """Hallie had dance practice for 1 hour on Tuesdays and 2 hours on Thursdays. On Saturdays, she had dance practice that lasted twice as long as Tuesday's night class. How many hours a week did she have dance practice?"""
    tuesday_hours = 1
    thursday_hours = 2
    saturday_hours = 2 * tuesday_hours
    total_hours = tuesday_hours + thursday_hours + saturday_hours
    result = total_hours
    return result

print(solution())