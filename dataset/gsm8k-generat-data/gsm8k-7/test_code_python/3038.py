def solution():
    distance = 4000  # parsecs
    num_earth_days = 24  # typical earth day is 24 hours
    travel_time = 2 * num_earth_days - 8  # hours
    avg_speed = distance / travel_time
    result = avg_speed
    return result

print(solution())