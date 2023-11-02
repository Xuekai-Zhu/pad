def solution():
    """Every hour past noon shadows from a building stretch an extra 5 feet, starting at zero at noon.  How long are the shadows from the building 6 hours past noon in inches?"""
    # Define length conversion factors
    FEET_TO_INCHES = 12

    # Define shadow growth rate in feet per hour
    GROWTH_RATE = 5

    # Define starting shadow length in feet
    STARTING_LENGTH = 0

    # Calculate shadow length in feet
    shadow_length_feet = STARTING_LENGTH + (GROWTH_RATE * 6)

    # Convert shadow length to inches
    shadow_length_inches = shadow_length_feet * FEET_TO_INCHES

    # Display shadow length in inches
    result = shadow_length_inches
    return result

print(solution())