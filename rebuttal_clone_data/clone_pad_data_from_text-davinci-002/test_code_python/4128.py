def solution():
    minutes_to_fill_car = 15
    minutes_to_drive = 30
    total_trips = 6
    total_minutes = minutes_to_fill_car + minutes_to_drive + total_trips
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())