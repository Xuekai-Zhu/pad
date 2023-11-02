def solution():
    breaths_per_minute = 17  # Ross takes 17 breaths per minute
    liters_per_breath = 5/9  # Ross inhales 5/9 of a liter with each breath

    # Calculate the total volume of air inhaled per minute
    volume_per_minute = breaths_per_minute * liters_per_breath

    # Calculate the total volume of air inhaled per day
    volume_per_day = volume_per_minute * 60 * 24  # 60 minutes per hour, 24 hours per day

    result = volume_per_day
    return result

print(solution())