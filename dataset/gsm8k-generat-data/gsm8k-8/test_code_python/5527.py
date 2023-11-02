def solution():
    # Determine the height of each platform using the distance fallen and number of falls
    height_per_fall = 4 * 4  # Walter falls 4 meters past David
    total_falls = 4  # Walter falls for 3 more times that depth before hitting the ground
    height_per_platform = height_per_fall / total_falls

    # Determine the platform number that David was on
    walter_platform = 8  # Walter fell from the eighth platform
    david_platform = walter_platform - 1 - height_per_fall // height_per_platform

    result = david_platform
    return result

print(solution())