def solution():
    lap_time = 42
    last_year_time = 47.25
    lap_distance = 3/4
    last_year_avg_mile_time = last_year_time / 7
    this_year_avg_mile_time = lap_time / 7
    difference = this_year_avg_mile_time - last_year_avg_mile_time
    result = difference
    return result

print(solution())