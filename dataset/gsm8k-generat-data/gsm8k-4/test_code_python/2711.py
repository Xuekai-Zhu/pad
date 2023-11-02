def solution():
    """Ross takes 17 breaths per minute by inhaling 5/9 liter of air to his lungs. What is the volume of air inhaled in 24 hours?"""
    # Define the number of breaths per minute and the volume of air inhaled per breath
    breaths_per_minute = 17
    volume_per_breath = 5/9

    # Convert minutes to hours and multiply by the number of breaths per hour
    breaths_per_hour = breaths_per_minute * 60
    breaths_per_day = breaths_per_hour * 24

    # Calculate the total volume of air inhaled in 24 hours
    volume_per_day = breaths_per_day * volume_per_breath

    # Return the result in liters
    result = volume_per_day
    return result

print(solution())