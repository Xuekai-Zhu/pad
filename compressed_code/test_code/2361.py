def solution():
    
    typical_earth_day_hours = 24
    voyage_hours = 2 * typical_earth_day_hours - 8
    distance = 4000
    speed = distance / voyage_hours
    result = speed
    return result

print(solution())