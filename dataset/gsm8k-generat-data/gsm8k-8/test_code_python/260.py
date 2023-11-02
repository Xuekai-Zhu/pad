def solution():
    # Each hour past noon, the shadow increases by 5 feet or 60 inches
    # Therefore, 6 hours past noon, the shadow will be 6*60 = 360 inches

    # Convert the length of the shadow from inches to feet and round to 2 decimal places
    shadow_length_feet = round(360/12, 2)

    result = shadow_length_feet
    return result

print(solution())