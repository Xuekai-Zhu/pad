def solution():
    breaths_per_minute = 17
    volume_per_breath = 5/9  # in liters

    # Calculate the volume of air inhaled in one hour
    volume_per_hour = breaths_per_minute * 60 * volume_per_breath

    # Calculate the volume of air inhaled in 24 hours
    volume_per_day = volume_per_hour * 24
    result = volume_per_day
    return result

print(solution())