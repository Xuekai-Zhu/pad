def solution():
    """Ross takes 17 breaths per minute by inhaling 5/9 liter of air to his lungs. What is the volume of air inhaled in 24 hours?"""
    breaths_per_minute = 17
    liters_per_breath = 5/9
    minutes_per_hour = 60
    hours_per_day = 24
    total_breaths_per_day = breaths_per_minute * minutes_per_hour * hours_per_day
    total_volume = total_breaths_per_day * liters_per_breath
    result = total_volume
    return result

print(solution())