def solution():
    """Some friends went hiking for 3.5 hours. They traveled 21 kilometers in that time. Birgit was 4 minutes/km faster than the average time. If Birgit kept the same pace, how many minutes would it take her to go 8 kilometers?"""
    total_hours = 3.5
    total_km = 21
    avg_time_per_km = total_hours / (total_km / 1.0)
    birgit_avg_time_per_km = avg_time_per_km - (4 / 60.0)
    time_for_8km = birgit_avg_time_per_km * 8
    result = int(time_for_8km * 60)
    return result

print(solution())