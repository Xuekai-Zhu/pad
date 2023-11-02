def solution():
    """Sandy walked from Holloway Shores to Sun Valley Shores for 8 hours on a particular day. She also walked half as many hours on the second day as she walked on the first day, to Hollock valley shores. Calculate the total time Sandy took to walk in the two days in minutes."""
    hours_day1 = 8
    hours_day2 = hours_day1 / 2
    total_hours = hours_day1 + hours_day2
    minutes_per_hour = 60
    total_minutes = total_hours * minutes_per_hour
    result = total_minutes
    return result

print(solution())