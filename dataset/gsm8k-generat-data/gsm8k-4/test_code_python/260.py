def solution():
    """Every hour past noon shadows from a building stretch an extra 5 feet, starting at zero at noon. How long are the shadows from the building 6 hours past noon in inches?"""
    # Define the length of the building in feet
    building_length = 100

    # Calculate the length of the shadow in feet 6 hours past noon
    shadow_length = building_length + (5 * 6)

    # Convert shadow length to inches
    shadow_length_inches = shadow_length * 12

    result = shadow_length_inches
    return result

print(solution())