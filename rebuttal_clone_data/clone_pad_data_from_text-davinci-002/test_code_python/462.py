def solution():
   Roberto_skips_per_hour = 4200
    Valerie_skips_per_minute = 80
    minutes = 15
    Roberto_skips = Roberto_skips_per_hour / 60 * minutes
    Valerie_skips = Valerie_skips_per_minute * minutes
    total_skips = Roberto_skips + Valerie_skips
    result = total_skips
    return result

print(solution())