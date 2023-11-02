def solution():
    pages_per_hour = 40
    hours_read_per_week = 600 / pages_per_hour
    new_reading_speed = pages_per_hour * 1.5
    new_hours_read_per_week = hours_read_per_week - 4
    new_pages_read_per_week = new_reading_speed * new_hours_read_per_week
    result = new_pages_read_per_week
    return result

print(solution())