def solution():
    breaths_per_minute = 17
    volume_per_breath = 5/9  # liters
    minutes_per_day = 24 * 60
    total_breaths = breaths_per_minute * minutes_per_day
    total_volume = total_breaths * volume_per_breath
    result = total_volume
    return result

print(solution())