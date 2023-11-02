def solution():
    # Calculate the length of the shadow at noon
    noon_shadow_length = 0

    # Calculate the length of the shadow 6 hours past noon
    hours_past_noon = 6
    extra_feet_per_hour = 5
    total_extra_feet = hours_past_noon * extra_feet_per_hour
    total_length = noon_shadow_length + total_extra_feet
    length_in_inches = total_length * 12  # Convert feet to inches

    result = length_in_inches
    return result

print(solution())