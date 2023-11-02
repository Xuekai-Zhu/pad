def solution():
    optimal_temp_range = range(70, 86)
    latitude = 75
    if latitude < 66.5 or latitude > 90:
        # Check if the latitude is outside the range where cauliflower can grow well
        result = "no"
    else:
        result = "yes"
    return result

print(solution())