def solution():
    breaths_per_minute = 17
    volume_per_breath = 5/9
    
    # Convert breaths per minute to breaths per day
    breaths_per_day = breaths_per_minute * 60 * 24
    
    # Calculate the total volume of air inhaled per day
    total_volume = breaths_per_day * volume_per_breath
    
    result = total_volume
    return result

print(solution())