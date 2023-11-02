def solution():
    max_wind_speed_solo = 14
    max_wind_speed_hurricane = 74
    if max_wind_speed_solo < max_wind_speed_hurricane:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())