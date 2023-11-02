def solution():
    """Every hour past noon shadows from a building stretch an extra 5 feet, starting at zero at noon. How long are the shadows from the building 6 hours past noon in inches?"""
    height_of_building = 20 # let's assume the height of the building is 20 feet
    increase_per_hour = 5
    time_past_noon = 6
    total_increase = increase_per_hour * time_past_noon
    shadow_length = height_of_building + total_increase # in feet
    shadow_length_inches = shadow_length * 12 # converting feet to inches
    result = shadow_length_inches
    return result

print(solution())