def solution():
    """Ross takes 17 breaths per minute by inhaling 5/9 liter of air to his lungs. What is the volume of air inhaled in 24 hours?"""
    # Define the number of breaths Ross takes per minute
    breaths_per_minute = 17

    # Define the volume of air inhaled per breath
    air_per_breath = 5/9

    # Calculate the volume of air inhaled per minute
    air_per_minute = breaths_per_minute * air_per_breath

    # Calculate the volume of air inhaled per day (24 hours)
    air_per_day = air_per_minute * 60 * 24

    # Display the volume of air inhaled per day
    result = air_per_day
    return result

print(solution())