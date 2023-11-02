def solution():
    butterfly_hours = 3
    backstroke_hours = 2
    butterfly_days = 4
    backstroke_days = 6
    minutes_in_an_hour = 60
    minutes_in_a_week = minutes_in_an_hour * 24 * 7
    minutes_in_a_month = minutes_in_a_week * 4
    butterfly_minutes = butterfly_hours * butterfly_days * minutes_in_an_hour
    backstroke_minutes = backstroke_hours * backstroke_days * minutes_in_an_hour
    total_minutes = butterfly_minutes + backstroke_minutes
    result = total_minutes
    return result

print(solution())