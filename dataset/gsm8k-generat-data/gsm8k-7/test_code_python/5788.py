def solution():
    total_time = 3.5  # hours
    distance = 21  # kilometers
    avg_speed = distance / total_time  # kilometers per hour
    avg_time_per_km = 1 / avg_speed * 60  # minutes per kilometer
    birgit_time_per_km = avg_time_per_km - 4  # minutes per kilometer for Birgit
    birgit_time_for_8km = 8 * birgit_time_per_km  # total time in minutes for Birgit to do 8 kilometers
    result = birgit_time_for_8km
    return result

print(solution())