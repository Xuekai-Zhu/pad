def solution():
    total_minutes = 20 * 30  # total number of minutes in all the episodes
    total_hours = total_minutes / 60  # total number of hours to finish the show
    hours_a_day = total_hours / 5  # hours needed to watch per day for 5 days
    result = hours_a_day
    return result

print(solution())