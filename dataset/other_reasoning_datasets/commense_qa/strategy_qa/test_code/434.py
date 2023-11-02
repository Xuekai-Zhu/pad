def solution():
    monday_night_football_start_time = "8pm EST"
    wwe_raw_air_time = "8pm-11pm EST on Monday nights"
    if monday_night_football_start_time == wwe_raw_air_time:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())