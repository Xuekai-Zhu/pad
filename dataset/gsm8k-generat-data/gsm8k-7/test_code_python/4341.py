def solution():
    day1_duration = 10  # in hours
    day2_duration = day1_duration + 2
    day3_duration = day2_duration * 2

    total_rain_duration = day1_duration + day2_duration + day3_duration
    result = total_rain_duration
    return result

print(solution())