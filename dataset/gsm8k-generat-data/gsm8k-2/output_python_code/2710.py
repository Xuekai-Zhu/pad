def solution():
    """Ross takes 17 breaths per minute by inhaling 5/9 liter of air to his lungs. What is the volume of air inhaled in 24 hours?"""
    breaths_per_minute = 17
    air_per_breath = 5/9
    minutes_per_day = 24 * 60
    total_breaths = breaths_per_minute * minutes_per_day
    total_air = total_breaths * air_per_breath
    result = total_air
    return result

print(solution())