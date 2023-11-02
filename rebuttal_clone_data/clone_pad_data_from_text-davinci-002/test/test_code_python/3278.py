def solution():
    total_hours = 3.5
    total_kilometers = 21
    Birgit_minutes = 4
    total_minutes = total_hours * 60
    average_speed = total_minutes / total_kilometers
    Birgit_time = 8 * (average_speed - Birgit_minutes)
    result = Birgit_time
    return result

print(solution())